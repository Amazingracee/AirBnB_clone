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
        Filestorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        """Serialzes __objects to JSON file."""
        serial_dict = FileStorage.__objects
        new_dict = {key: serial_dict[key].to_dict() for key in serial_dict.keys()}
        
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path) as file:
                new_dict = json.load(file)
        except FileNotFoundError:
            return
