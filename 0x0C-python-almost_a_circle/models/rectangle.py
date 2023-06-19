#!/usr/bin/python3
"""
File: rectangle.py
Desc: This module contains a class; Rectangle
"""

from models.base import Base


def check_value(name, value, sides=True):
    """
    Checks if correct input was inserted
    """
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if sides:
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
    elif value < 0:
        raise ValueError("{} must be >= 0".format(name))


class Rectangle(Base):
    """
    Representation of the class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialization of the object
        """
        self._width = None
        self._height = None
        self._x = None
        self._y = None
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        String representation of class
        """
        return (
            f"[Rectangle] ({self.id}) {self._x}/{self._y} - {self._width}/{self._height}"
        )

    @property
    def width(self):
        """
        getter for width
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        Sets the value for width
        """
        check_value("width", value)
        self._width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self._height

    @height.setter
    def height(self, value):
        """
        Sets the value for height
        """
        check_value("height", value)
        self._height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self._x

    @x.setter
    def x(self, value):
        """
        Sets the value for x
        """
        check_value("x", value, False)
        self._x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self._y

    @y.setter
    def y(self, value):
        """
        Sets the value for y
        """
        check_value("y", value, False)
        self._y = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self._width * self._height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'
        """
        print("\n" * self._y, end='')
        for i in range(self._height):
            print((' ' * self._x) + ('#' * self._width) + '\n', end='')
