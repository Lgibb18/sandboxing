import Scripts.Engine.commands as commands

class PrintCommand:
    def __init__(self, name):
        commands.all_commands[name] = self

    def process(self, args : list):
        print(*args)


Command = PrintCommand("print")