#!/usr/bin/python3
"""
Class Rectangle
Created: July 17, 2023
By: Chepkiyeng Alexander
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.
        atributes:
        width: width of rectangle
        height: height of rectangle
        x: private value
        y: private value
        id: private value inherits from base
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        property method for width
        Return: value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter method for width
        Return: new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        property method for height
        Return: value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter method for height
        Return: value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        property method for x
        Return: value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter method for x
        Return: value of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        property method for y
        Return: value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter method for y
        Return: value of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method that calculates the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        method that prints the rectangle with the character #.
        """
        for row in range(self.__y):
            print("\n", end="")
        for h in range(self.__height):
            for column in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """
        string representation
        """
        str_msg = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                          self.__y,
                                                          self.__width,
                                                          self.__height)
        return (str_msg)

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes.
        """
        if not args or args is None:
            for attrib_name, attrib_value in kwargs.items():
                setattr(self, attrib_name, attrib_value)

        else:
            attrib_name = ["id", "width", "height", "x", "y"]
            attrib_value = []
            for value in args:
                attrib_value.append(value)
                for i in range(len(attrib_value)):
                    setattr(self, attrib_name[i], attrib_value[i])

    def to_dictionary(self):
        """
        dictionary representation
        """
        dict_repr = {'x': self.x, 'y': self.y, 'id': self.id,
                     'height': self.height, 'width': self.width}
        return dict_repr
