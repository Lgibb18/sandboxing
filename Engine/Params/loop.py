update_methods = []
def sign_update(method): update_methods.append(method)
def unsign_update(method): update_methods.remove(method)

draw_methods = []
def sign_draw(method): draw_methods.append(method)
def unsign_draw(method): draw_methods.remove(method)

logic_methods = []
def sign_logic(method): logic_methods.append(method)
def unsign_logic(method): logic_methods.remove(method)

from Engine.Utilities.logger import *

def Update(f):
    sign_update(f)
    return f

def Draw(f):
    sign_draw(f)
    return f

def Logic(f):
    sign_logic(f)
    return f