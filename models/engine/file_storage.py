#!/usr/bin/python3
"""Module contain class FileStorage."""
import os
import json


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances.

    Private class attributes:
        - __file_path
        - __objects

    Public instance methods
        - all
        - new
        - save
        - reload
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to a JSON file."""
        json_dict = {}
        for key, obj in FileStorage.__objects.items():
            json_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
            for key, value in json_dict.items():
                class_name, obj_id = key.split('.')
                obj_class = globals()[class_name]
                obj = obj_class(**value)
                FileStorage.__objects[key] = obj
