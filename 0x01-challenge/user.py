#!/usr/bin/python3
"""manipulating user info"""


class User:
    """User class"""

    def init(self):
        self.email = None

    @property
    def email(self):
        """Email property getter"""
        return self.__email

    @email.setter
    def email(self, value):
        """Email property setter"""
        if not isinstance(value, str):
            raise TypeError("Email must be a string")
        self.__email = value
