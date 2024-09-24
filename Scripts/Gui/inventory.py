import Engine.Scripts.events as events
from Engine.Scripts.entities import *
from Engine.Scripts.camera import *
import Engine.Utilities.sprites as sprites
from Engine.Utilities.sprites import *
from Engine.Utilities.utils import *
import pygame_gui
from pygame_gui.elements import *
from Engine.Params.loop import *
from Engine.Utilities.logger import *
from Engine.Params.manager import *
import Engine.Scripts.events
from pygame_gui.core.ui_element import UIElement
from typing import Union, Dict
from pygame_gui.core.gui_type_hints import Coordinate, RectLike
from Engine.Params.settings import *
from Engine.Params.runtime import runtime
from Engine.Scripts.component import *
from Scripts.Components.SpriteComponent import *
BUTTON_SIZE = 70
IMAGE_SIZE = BUTTON_SIZE / 1.4
class Cell:
    def __init__(self, relative_rect : Union[RectLike, Coordinate], entity, parent : UIElement, anchors: Dict[str, str | UIElement] = {}):
        global BUTTON_SIZE, IMAGE_SIZE
        self.entity = entity
        self.button = UIButton(relative_rect=relative_rect, text="", anchors=anchors, container=parent.get_container(), object_id="#inv_button")
        self.image = UIImage(relative_rect=pg.Rect((BUTTON_SIZE - IMAGE_SIZE)/2, (BUTTON_SIZE - IMAGE_SIZE)/2, IMAGE_SIZE, IMAGE_SIZE), image_surface=entity.entity.icon, parent_element=self.button, container=parent.get_container(), 
                               anchors = anchors)
        if type(self.image.image) is pg.surface.Surface:
            self.image.set_image(pg.transform.scale(entity.entity.icon, (64, 64)), False)
    
    def is_clicked(self) -> bool:
        for event in events.event_list:
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.button:
                    return True
        return False

class Row:
    def __init__(self, parent : UIElement, prev_row : UIElement | None = None):
        global BUTTON_SIZE
        sign_update(self.update)
        resolution = pg.display.get_window_size()
        self._cells : list[Cell] = []
        self.panel = UIPanel(
            (0, 5, ((resolution[0] / 5) // BUTTON_SIZE) * BUTTON_SIZE, BUTTON_SIZE-5),
            anchors={
                'centerx': 'centerx'
            },
            margins={'left': 0, 'right': 0, 'top': -3, 'bottom': -3},
            container=parent.get_container(),
            object_id="#inv_row"
        )
        if prev_row != None:
            self.panel.set_anchors({
                'centerx': 'centerx',
                'top_target': prev_row
            })

    def update(self):
        resolution = pg.display.get_window_size()
        self.panel.set_dimensions((((resolution[0] / 5) // BUTTON_SIZE) * BUTTON_SIZE, BUTTON_SIZE-5))


    def add_cell(self, entity):
        cell = Cell(pg.Rect(0, 0, BUTTON_SIZE, BUTTON_SIZE), entity, self.panel)
        if len(self._cells) > 0:
            cell.button.set_anchors({
                'left_target': self._cells[-1].button
            })
            self._cells.append(cell)
            cell.image.set_anchors({
                'left_target': self._cells[-2].button,
            })
        else: self._cells.append(cell)
        return cell


class Inventory:
    def __init__(self) -> None:
        self.grid = Instantiate("grid", Transform())
        for comp in self.grid.components:
            if comp.__class__.__name__ == "SpriteComponent":
                self.grid_sprite = comp
        sign_update(self.update)
        resolution = pg.display.get_window_size()
        self.enabled = True
        self.selected_entity : Entity
        self.cells = []
        self.rect = pg.Rect(0, 0, resolution[0] / 5, resolution[1])
        self.panel = UIPanel(self.rect, manager=manager.manager,
            margins={'left': 0, 'right': 0, 'top': 3, 'bottom': 3}, object_id="#inv_tab",
            anchors={"centery": "centery"})
        self.max_row_length = (resolution[0] / 5) / BUTTON_SIZE
        self.rebuild()

    rows : list[Row] = []
    def rebuild(self):
        global BUTTON_SIZE, IMAGE_SIZE
        BUTTON_SIZE = Settings.buttonSize
        IMAGE_SIZE = BUTTON_SIZE / 1.4
        self.cells : list[Cell] = []
        for row in self.rows:
            row.panel.kill()
        self.rows = []
        if not self.enabled: return
        resolution = pg.display.get_window_size()
        row = Row(self.panel)
        self.rows.append(row)
        i = 0
        for entity in all_entities.values():
            if not entity.canBeInMenu: continue
            i += 1
            if i > self.max_row_length:
                row = Row(self.panel, row.panel)
                self.rows.append(row)
                i = 1
            self.cells.append(row.add_cell(entity))
        manager.manager.set_window_resolution((resolution[0], resolution[1]))
        self.selected_entity = self.cells[0].entity

    def update(self):
        self.grid_sprite.visible = runtime.grid_placing
                
        resolution = pg.display.get_window_size()
        self.max_row_length = (resolution[0] / 5) // BUTTON_SIZE
        for cell in self.cells:
            if cell.is_clicked():
                self.selected_entity = cell.entity

        for event in events.event_list:
            if event.type == pg.VIDEORESIZE:
                    self.panel.set_dimensions((event.w / 5, event.h))
                    self.rebuild()
        for (_, key) in events.keyboard_list:
            if key == pg.K_e:
                if self.selected_entity != None:
                    pos = camera.mouse_pos()
                    if runtime.grid_placing:
                        pos = (
                            ((pos[0]+25) // 50) * 50,
                            ((pos[1]+25) // 50) * 50
                        )
                    self.selected_entity.instantiate(Transform(pos))
            if key == pg.K_TAB:
                self.enabled = not self.enabled
                for row in self.rows:
                    for cell in row._cells:
                        cell.button.visible = self.enabled
                        cell.image.visible = self.enabled
