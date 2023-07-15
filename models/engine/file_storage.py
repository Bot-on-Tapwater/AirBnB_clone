#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects[f"{class_name}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        non_ser_dict = FileStorage.__objects
        ser_dict = {}

        for obj_id in non_ser_dict.keys():
            ser_dict[obj_id] = non_ser_dict[obj_id].to_dict()

        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(ser_dict, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as json_file:
                ser_dict = json.load(json_file)
                for values in ser_dict.values():
                    cls_name = values["__class__"]
                    del values["__class__"]
                    self.new(eval(cls_name)(**values))

        except FileNotFoundError:
            return
