#!/usr/bin/python3
"""Module contains class BaseModel."""
import uuid
from datetime import datetime

class BaseModel:
    """Defines all common attributes/methods for other classes.

    Public instance attributes:
        - id
        - created_at
        - updated_at

    Public instance methods:
        - save: updates 'updated_at'
        - to_dict
    """

    def __init__(self):
        """Constructor for class BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__(self):
        """Returns a human-readable string representation of an instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of an instance."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.datetime.isoformat()
        instance_dict['updated_at'] = self.updated_at.datetime.isoformat()
