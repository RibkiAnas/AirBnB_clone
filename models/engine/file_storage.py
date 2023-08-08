#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}
    
    @staticmethod
    def classes():
        return ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

    @staticmethod
    def all():
        return FileStorage.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    @staticmethod
    def save():
        dict_ = {}
        for k, v in FileStorage.__objects.items():
            dict_[k] = v.to_dict()
        with open(FileStorage.__file_path, mode="w+") as file:
            return file.write(json.dumps(dict_))

    def reload(self):
        json_d = {}
        classes = {"BaseModel": BaseModel}

        with open(self.__file_path, mode="r") as file:
            json_d = json.load(file)
        if json_d != {}:
            for k, v in json_d.items():
                key = classes.get(k.split('.')[0])
                self.__objects[k] = key(**v)
