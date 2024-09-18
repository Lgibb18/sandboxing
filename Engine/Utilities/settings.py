import pygame as pg
import json
path = "Assets/Settings/settings.json"
class __Settings:
    def __init__(self):
        self.steps = 10
        self.targetFps = 60
        self.load()

    def load_from_dict(self, d):
        for key, value in d.items():
            setattr(self, key, value)

    def save(self):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self, 
                      f, 
                      sort_keys=True, 
                      ensure_ascii=False, 
                      indent=4, 
                      default=lambda o: o.__dict__)
            
    def load(self):
        try:
            with open(path, 'r', encoding='utf-8', ) as f:
                data = f.read()
                self.load_from_dict(json.loads(data))
        except FileNotFoundError as e:
            print(f"Creating a new options.json")
            self.save()
        except ValueError as e:
            print(f"Settings was broken. Creating a new options.json")
            self.save()


Settings = __Settings()
