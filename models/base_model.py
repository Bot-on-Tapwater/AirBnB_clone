#!/usr/bin/python3

"""
Create class BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at':
                        datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, datetime_obj)
                    elif key == 'updated_at':
                        datetime_obj = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, datetime_obj)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        String representation
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates attr updated_at with current time
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns dictionary of key values of instance
        """
        my_dict = self.__dict__.copy()
        # my_dict['id'] = self.id
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
