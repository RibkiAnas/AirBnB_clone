#!/usr/bin/python3
"""
class BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class for all other classes
    """

    def __init__(self, *args, **kwargs):
        """The BaseModel init method"""

        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String Representation of BaseModel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Saves object"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object"""
        tdict = self.__dict__.copy()

        tdict["created_at"] = self.created_at.isoformat()
        tdict["updated_at"] = self.updated_at.isoformat()
        tdict["__class__"] = self.__class__.__name__

        return tdict
