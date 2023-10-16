#!/usr/bin/python3
"""instances of a defined class"""


class Square():
    """square class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def Permiter_Of_My_Square(self):
        """perimetter of a square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representaton of area or perimeter"""
        return "{}/{}".format(self.width, self.height)
