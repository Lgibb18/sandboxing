__info = '\033[97m'
__debug = '\033[96m'
__warn = '\033[93m'
__error = '\033[91m'
__fatal = '\033[95m'
__reset = '\033[0m'

_print = print

def __get_invoker() -> str:
        from inspect import stack
        try:
            _stack = stack()
            _class = _stack[2][0].f_locals["self"].__class__.__name__
            return f" {_class}"
        except:
            return ""

def info(text):
    to_print = f"{__info}[INFO]{__reset}{__get_invoker()}: {text}"
    _print(to_print)
def debug(text):
    to_print = f"{__debug}[DEBG]{__reset}{__get_invoker()}: {text}"
    _print(to_print)
def warn(text):
    to_print = f"{__warn}[WARN]{__reset}{__get_invoker()}: {text}"
    _print(to_print)
def error(text):
    to_print = f"{__error}[ERRO]{__reset}{__get_invoker()}: {text}"
    _print(to_print)
def fatal(text, exit : bool = True):
    to_print = f"{__fatal}[FATL]{__reset}{__get_invoker()}: {text}"
    _print(to_print)
    if(exit):
        import pygame
        pygame.quit()

INFO = 0
DEBUG = 1
WARN = 2
ERROR = 3
FATAL = 4

def print(text, type: int = INFO):
    match type:
        case 0:
            info(text)
        case 1:
            debug(text)
        case 2:
            warn(text)
        case 3:
            error(text)
        case 4:
            fatal(text)
