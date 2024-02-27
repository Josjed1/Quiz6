# shape.py
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass


# circle.py
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius


# square.py
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length * self.side_length


# rectangle.py
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


# shape_factory.py
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "Square":
            return Square(*args)
        elif shape_type == "Rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("Invalid shape type")


# o.py
def main():
    # Example usage
    shapes = [
        ShapeFactory.create_shape("Circle", 5),
        ShapeFactory.create_shape("Square", 4),
        ShapeFactory.create_shape("Rectangle", 3, 6),
        # Add new shapes without modifying existing code
        ShapeFactory.create_shape("Triangle", 3, 4, 5)  # Example of adding a new shape
    ]

    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.get_area()}")


if __name__ == "__main__":
    main()
