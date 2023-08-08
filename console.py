#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, sta):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, sta):
        """EOF end of file to exit"""
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
