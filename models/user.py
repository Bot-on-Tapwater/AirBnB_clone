#!/usr/bin/python3

"""
Create class User
"""

from models import base_model


class User(base_model.BaseModel):
    """
    class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
