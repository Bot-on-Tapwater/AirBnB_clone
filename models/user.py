#!/usr/bin/python3

"""
Create class User
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
