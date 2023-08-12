#!/usr/bin/python3
"""This module defines a class to manage file storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """This class manages storage in JSON format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retrieves a Dictionary of Stored Models"""
        return self.__objects

    def new(self, obj):
        """Inserts new object into storage dictionary"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        dict_ = {}
        for k, v in self.__objects.items():
            dict_[k] = v.to_dict()
        with open(self.__file_path, mode="w+") as file:
            return file.write(json.dumps(dict_))

    def reload(self):
        """Loads storage dictionary from file"""
        json_d = {}
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        with open(self.__file_path, mode="r") as file:
            json_d = json.load(file)
        if json_d != {}:
            for k, v in json_d.items():
                key = classes.get(k.split('.')[0])
                self.__objects[k] = key(**v)
