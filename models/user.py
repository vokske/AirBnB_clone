#!/usr/bin/python3
"""Module contains the class User."""
from models.base_model import BaseModel


class User(BaseModel):
    """Contains common attributes for a user

    Public class attributes:
        - email
        - password
        - first_name
        - last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
