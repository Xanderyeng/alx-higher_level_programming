#!/usr/bin/python3
"""
class Base
Created: July 17, 2023
By: Chepkiyeng Alexander
"""
import json


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.
        atributes:
        id: integer from id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        attributes:
        list_dictionary.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        file_name = cls.__name__ + ".json"
        lines = []
        if list_objs is not None:
            for i in list_objs:
                lines.append(cls.to_dictionary(i))
        with open(file_name, mode="w") as f:
            f.write(cls.to_json_string(lines))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(3, 4)
        elif cls.__name__ is "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        file_name = cls.__name__ + ".json"
        json_obj = []
        try:
            with open(file_name, "r") as f:
                json_obj = cls.from_json_string(f.read())
            for key, value in enumerate(json_obj):
                json_obj[key] = cls.create(**json_obj[key])
        except:
            pass
        return json_obj
