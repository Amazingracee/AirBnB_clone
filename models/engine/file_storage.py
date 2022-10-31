#!/usr/bin/python3
"""Module for FileStorage class"""
from models.base_model import BaseModel
import json

class FileStorage:
    """Class that serializes basemodel instances."""
    __filepath = file.json
    __objects = {}

    def all(self):
        """returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj
    
    def save(self):
        """ serializes __objects to the JSON file """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            serial_dict = FileStorage.__objects.copy()
            for key, value in FileStorage.__objects.items():
                serial_dict[key] = value.to_dict()
            json.dump(serial_dict, f)

    def reload(self):
        """Deserializes the JSON in __file_path if it exists"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                deserial = json.load(f)
                for base_dict in deserial.values():
                    name = base_dict["__class__"]
                    del base_dict["__class__"]
                    self.new(eval(name)(**base_dict))
        except FileNotFoundError:
            return
