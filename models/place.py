#!/usr/bin/python3

"""
Create class Place
"""

from models import base_model


class Place(base_model.BaseModel):
    """
    class Place
    """
    city_id = "Place_hol"
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