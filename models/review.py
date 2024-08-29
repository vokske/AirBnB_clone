#!/usr/bin/python3

"""Module contains class Review."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Public class attributes:
        - place_id
        - user_id
        - text
    """
    place_id = ""
    user_id = ""
    text = ""
