from pymunk import Vec2d


def flipy(p):
    return Vec2d(p[0], -p[1]+800)