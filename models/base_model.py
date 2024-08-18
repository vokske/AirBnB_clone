#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:

    """ Class BaseModel
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Initialize a Base instance.

        Args:
            - *args: List of arguments to the function
            - **kwargs: Keyworded list of arguments (dict) to the function
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    def __str__(self):
        """Return a human-readable string representation of a class instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """Updates the public instance attribute 'updated_at'
        with the current datetime.
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """Returns a dict representation of the instance."""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
