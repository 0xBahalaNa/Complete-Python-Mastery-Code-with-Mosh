"""
7. Classes, 20. Duck Typing

Polymorphic behavior.
Define a base class.
Define a common method amongst the children classes.

Methods that take on different forms.

Python is dynamically typed language. 

Duck typing.
Python only looks for the existence of the draw method.
Don't need a base class. 
"""

from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()
