#!/usr/bin/python3
"""Module contains class Place."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a place.

    Public Class Attributes:
        - city_id: City.id
        - user_id: User.id
        - name
        - description
        - number_rooms
        - number_bathrooms
        - max_guest
        - price_by_night
        - latitude
        - longitude
        - amenity_ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
