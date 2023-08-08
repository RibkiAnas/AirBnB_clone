#!/usr/bin/python3
"""
class BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class
    """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        tdict = self.__dict__.copy()

        tdict["created_at"] = self.created_at.isoformat()
        tdict["updated_at"] = self.updated_at.isoformat()
        tdict["__class__"] = self.__class__.__name__

        return tdict
