info = '\033[97m'
debug = '\033[96m'
warn = '\033[93m'
error = '\033[91m'
fatal = '\033[95m'
reset = '\033[0m'


class _logger:
    def __get_invoker(self) -> str:
        from inspect import stack
        try:
            _stack = stack()
            _class = _stack[2][0].f_locals["self"].__class__.__name__
            return f" {_class}"
        except:
            return ""


    def info(self, text):
        to_print = f"{info}[INFO]{reset}{self.__get_invoker()}: {text}"
        print(to_print)
    
    def debug(self, text):
        to_print = f"{debug}[DEBG]{reset}{self.__get_invoker()}: {text}"
        print(to_print)

    def warn(self, text):
        to_print = f"{warn}[WARN]{reset}{self.__get_invoker()}: {text}"
        print(to_print)

    def error(self, text):
        to_print = f"{error}[ERRO]{reset}{self.__get_invoker()}: {text}"
        print(to_print)

    def fatal(self, text, exit : bool = True):
        to_print = f"{fatal}[FATL]{reset}{self.__get_invoker()}: {text}"
        print(to_print)
        if(exit):
            import pygame
            pygame.quit()

Logger = _logger()