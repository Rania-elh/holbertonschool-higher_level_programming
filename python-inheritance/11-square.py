#!/usr/bin/python3
"""Class a square follow by rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Function that innitialize a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """method must be implemented an area"""
        return self.__size ** 2

    def __str__(self):
        """Method that prints string"""
        return f"[Square] {self.__size}/{self.__size}"
