#!/usr/bin/python3
# Author -- Gadoskey
"""This module defines a class Student"""


class Student:
    """A class student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with first and second names and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return self.__dict__
