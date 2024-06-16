import pygame as pg

class Commands:
    def __init__(self):
        pass

    def process_command(self, command : str):
        if len(command) < 1:
            return
        command_split = command.split(' ')
        command = command_split[0].lower()
        if len(command_split) > 1:
            args = command_split[1:]
        else:
            args = []
        if command in list(all_commands.keys()):
            return all_commands[command].process(args)


all_commands = {}
