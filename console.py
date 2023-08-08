#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id

        Args:
            arg: contains the name of the class and id to be created
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in FileStorage.classes():
            print("** class doesn't exist **")
        else:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id

        Args:
            arg: contains the class name and id to be printed
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in FileStorage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in FileStorage.all():
                print("** no instance found **")
            else:
                print(FileStorage.all()[key])
                
    def do_destroy(self, arg):
        """Delete an instance based on the class name and id

        Args:
            arg: contains the class name and id to be deleted
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in FileStorage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in FileStorage.all():
                print("** no instance found **")
            else:
                del FileStorage.all()[key]
                FileStorage.save()
                
    def do_all(self, arg):
        """Print all string representation of all instances based or not on the class name

        Args:
            arg: contains the class name to be printed
        """
        args = arg.split()
        if len(args) == 0:
            for value in FileStorage.all().values():
                print(value)
        elif args[0] not in FileStorage.classes():
            print("** class doesn't exist **")
        else:
            for key, value in FileStorage.all().items():
                if key.startswith(args[0]):
                    print(value)
                    
    def do_update(self, arg):
        """Update an instance based on the class name and id by adding or updating attribute

        Args:
            arg (): contains the class name and id to be updated
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in FileStorage.classes():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in FileStorage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = FileStorage.all()[key]
                setattr(obj, args[2], eval(args[3]))
                obj.save()

    def do_quit(self, sta):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, sta):
        """EOF end of file to exit"""
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
