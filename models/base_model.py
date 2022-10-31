#!/usr/bin/env python3
"""A module containing a class"""
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:
    """A BaseModel class that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) ({self.__dict__})"

    def save(self):
        """Updates 'updated_at' current datetime"""
        self.updated_at = datetime.now()
        storage.save()

        def to_dict(self):
            """Returns dictionary containing all keys/values"""
            instance_dict = self.__dict__.copy()
            instance_dict["__class__"] = self.__class__.__name__
            instance_dict["created_at"] = self.created_at.isoformat()
            instance_dict["updated_at"] = self.updated_at.isoformat()
            return instance_dict
