"""Compoiste Design Pattern Example"""
from abc import ABCMeta, abstractmethod

class IGraphic(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def print():
        """print information"""

class Triangle(IGraphic):
    def print(self):
        print("Triangle")
    def get_name(self):
        return "Triangle"

class Circle(IGraphic):
    def print(self):
        print("Circle")
    def get_name(self):
        return "Circle"

class Square(IGraphic):
    def print(self):
        print("Square")
    def get_name(self):
        return "Square"

class CompositeGraphic(IGraphic):
    def __init__(self):
        self.child_graphics = []

    def add(self, graphic):
        self.child_graphics.append(graphic)
        print(f"Object added to composite")

    def print(self):
        for g in self.child_graphics:
            g.print()


TRIANGLE1 = Triangle()
CIRCLE1 = Circle()
SQUARE1 = Square()

print("First Composite Object is initializing..")
COMPOSITE1 = CompositeGraphic()
COMPOSITE1.add(TRIANGLE1)
COMPOSITE1.add(SQUARE1)
print("First Composite Object Operations have been completed!\n")

print("Second Composite Object is initializing..")
COMPOSITE2 = CompositeGraphic()
COMPOSITE2.add(CIRCLE1)
COMPOSITE2.add(COMPOSITE1)
print("Second Composite Object Operations have been completed!\n")

print("I give you the First Composite Object: ")
COMPOSITE1.print()

print("I give you the Second Composite Object: ")
COMPOSITE2.print()
