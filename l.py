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

    def set_radius(self, radius):
        self.radius = radius


# rectangle.py

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height


# triangle.py

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height


# polygon.py
class Polygon(Shape):
    def __init__(self, sides_length):
        self.sides_length = sides_length

    def get_area(self):
        # Dummy logic for polygon area calculation
        # For demonstration purposes, let's assume it's the sum of the side lengths
        return sum(self.sides_length)


# l.py
def main():
    # Example usage
    shapes = [
        Circle(5),
        Rectangle(3, 6),
        Triangle(4, 5),
        # Adding a new Polygon shape without violating LSP
        Polygon([3, 4, 5, 6])
    ]

    for shape in shapes:
        print(f"Area of {shape.__class__.__name__}: {shape.get_area()}")


if __name__ == "__main__":
    main()
