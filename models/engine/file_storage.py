#!/usr/bin/python3

"""Module contains class FileStorage."""

class FileStorage(object):
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

    __file_path = ""
    __objects = {}


    def all(self):
        """Returns the '__objects' dictionary."""
        return FileStorage.__object


    def new(self, obj):
        """Sets the 'obj' with key '<obj class name>.id'
        in the __objects dictionary."""
        key = f"{type(obj).__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj


    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(FileStorage.__file_path, 'w') as f:



