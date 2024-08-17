#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel(object):

    """ Class BaseModel
    Defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialize a Base instance.

        Args:
            - *args: List of arguments to the function
            - **kwargs: Keyworded list of arguments (dict) to the function
        """
        dt_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], dt_format)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], dt_format)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """Return a human-readable string representation of a class instance."""
        return f"[{cls.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        """Updates the public instance attribute 'updated_at'
        with the current datetime.
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """Returns a dict representation of a class instance."""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = cls.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
