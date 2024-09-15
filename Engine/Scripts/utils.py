from pymunk import Vec2d
from ast import literal_eval

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


def collision_check_topleft(pos1, pos2, scale):
    if((pos1[0] > pos2[0])
            and (pos1[0] < pos2[0] + (scale[0]))
            and (pos1[1] > pos2[1])
            and (pos1[1] < pos2[1] + (scale[1]))):
        return True
    else:
        return False

def vec_diff(first : tuple, second : tuple):
    return (first[0] - second[0], first[1] - second[1])

def vec_add(first : tuple, second : tuple):
    return (first[0] + second[0], first[1] + second[1])

class convert:
    def __new__(self, text):
        self.text = text
        return self.__simplest(text)
    
    def type(text):
        return type(convert(text))

    def __simplest(text):
        try:
            return literal_eval(str(text))
        except:
            return text
