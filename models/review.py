#!/usr/bin/python3

"""
Create class Review
"""

from models import base_model


class Review(base_model.BaseModel):
    """
    class Review
    """
    place_id = ""
    user_id = ""
    text = ""
