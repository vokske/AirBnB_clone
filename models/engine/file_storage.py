#!/usr/bin/python3
"""Module contains class FileStorage."""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON files to instances.

    Private class attributes:
        __file_path: String representing the path to the JSON file.
        __objects: Dictionary that will store all objects by <class name>.id

    Public instance methods:
        - all(self)
        - new(self, obj)
        - save(self)
        - reload(self)
    """

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns the '__objects' dictionary."""
        return FileStorage.__objects


    def new(self, obj):
        """Sets the 'obj' with key '<obj class name>.id'
        in the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)


    def reload(self):
        """Deserializes the JSON file to __objects (
        only if the JSON file exists.)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)

            class_map = {
                    "BaseModel": BaseModel,
                    }

            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_class = class_map.get(class_name)
                if obj_class:
                    obj = obj_class(**value)
                    FileStorage.__objects[key] = obj
