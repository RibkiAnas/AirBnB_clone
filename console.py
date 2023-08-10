#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
import re
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb) "
    __classes = {"BaseModel": BaseModel, "User": User, "State": State,
                 "City": City, "Amenity": Amenity, "Place": Place,
                 "Review": Review}

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it and print the id

        Args:
            arg: contains the name of the class and id to be created
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__classes[args[0]]()
            print(obj.id)
            storage.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        """Print the string representation of an instance based
           on the class name and id

        Args:
            arg: contains the class name and id to be printed
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1].replace('"', "")
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\
              or <class name>.show(<id>)\n")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id

        Args:
            arg: contains the class name and id to be deleted
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1].replace('"', "")
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId> " +
              "or <class name>.destroy(<id>)\n")

    def do_all(self, arg):
        """Print all string representation of all instances
           based or not on the class name

        Args:
            arg: contains the class name to be printed
        """
        args = arg.split()
        objs = []
        if len(args) == 0:
            for value in storage.all().values():
                objs.append(value.__str__())
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
            return True
        else:
            for key, value in storage.all().items():
                if key.startswith(args[0]):
                    objs.append(value.__str__())
        print(objs)

    def help_all(self):
        """ Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className> or <className>.all()\n")

    def do_update(self, arg):
        """Update an instance based on the class name and id
           by adding or updating attribute

        Args:
            arg (): contains the class name and id to be updated
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                val = args[3]
                if '"' in val:
                    try:
                        i = 4
                        while True:
                            val += " " + args[i]
                            i += 1
                    except IndexError:
                        val = val.replace('"', "")
                setattr(obj, args[2], val)
                obj.save()

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>" +
              " or <class name>.update(<id>, <attribute name>," +
              " <attribute value>)\n")

    def default(self, line):
        """default command for handling <class name>.(actions)"""
        do_actions = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        match = re.search(r"\.", line)
        if match is not None:
            line_ = [line[:match.span()[0]], line[match.span()[1]:]]
            match = re.search(r"\(.*?\)", line_[1])
            if match is not None:
                command = [line_[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in do_actions.keys():
                    arg = "{} {}".format(line_[0], command[1])
                    do_actions[command[0]](arg)
            else:
                print("*** Unknown syntax: {}".format(line))

    def do_count(self, arg):
        """<class name>.count() Countes models"""
        args = arg.split()
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def help_count(self):
        """ Help information for the count command """
        print("Count all objects of a class")
        print("[Usage]: count <className> or <className>.count()\n")

    def emptyline(self):
        """repeats line on receiving empty line"""
        pass

    def do_quit(self, sta):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, sta):
        """EOF end of file to exit"""
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
