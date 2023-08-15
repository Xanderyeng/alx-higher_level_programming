#!/usr/bin/python3
"""
class for a Squar
Created July 17, 2023
By: Chepkiyeng Alexander
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class: Square that inherits from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor.
        Attributes:
        size: size of square
        x: int value
        y: int value
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation for square
        """
        str_msg = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                    self.y, self.size)
        return str_msg

    @property
    def size(self):
        """
        property method to get size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method to set size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes.
        """
        if not args or args is None:
            for attrib_name, attrib_value in kwargs.items():
                setattr(self, attrib_name, attrib_value)

        else:
            attrib_name = ["id", "size", "x", "y"]
            attrib_value = []
            for value in args:
                attrib_value.append(value)
                for i in range(len(attrib_value)):
                    setattr(self, attrib_name[i], attrib_value[i])

    def to_dictionary(self):
        """
        dictionary representation
        """
        dict_repr = {'id': self.id, 'x': self.x, 'size': self.size,
                     'y': self.y}
        return dict_repr
