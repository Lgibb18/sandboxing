from pymunk import Vec2d
import pygame as pg
import pymunk as pm
import math
import random
import pymunk.pygame_util
from Scripts.Engine.entity import *
def flipy(p):
    return Vec2d(p[0], -p[1]+800)


def collision_check(pos1, pos2, scale):
    if((pos1[0] > pos2[0] - (scale[0] / 2))
            and (pos1[0] < pos2[0] + (scale[0] / 2))
            and (pos1[1] > pos2[1] - (scale[1] / 2))
            and (pos1[1] < pos2[1] + (scale[1] / 2))):
        return True
    else:
        return False

def vec_diff(first : tuple, second : tuple):
    return (first[0] - second[0], first[1] - second[1])

def vec_add(first : tuple, second : tuple):
    return (first[0] + second[0], first[1] + second[1])