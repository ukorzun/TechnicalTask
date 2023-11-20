import logging
from abc import ABC, abstractmethod


class Engine2D:
    SUPPORTED_COLORS = ["black", "red", "green", "blue"]

    def __init__(self):
        self.canvas = []
        self.current_color = "black"
        self.logger = logging.getLogger("Engine2D")

    def add_shape(self, shape):
        self.canvas.append(shape)

    def set_color(self, color):
        if self.is_valid_color(color):
            self.logger.info(f"Setting color to: {color}")
            self.current_color = color
        else:
            self.logger.warning(f"Unsupported color: {color}. Keeping the current color: {self.current_color}")

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas.clear()

    def is_valid_color(self, color):
        return color in self.SUPPORTED_COLORS


class Shape(ABC):

    @abstractmethod
    def draw(self, color):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.__dict__ == other.__dict__)


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x, self.y, self.width, self.height = x, y, width, height

    def draw(self, color):
        print(
            f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} in {color} color")

    def __str__(self):
        return f"Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height}"


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1, self.x2, self.y2, self.x3, self.y3 = x1, y1, x2, y2, x3, y3

    def draw(self, color):
        print(
            f"Drawing Triangle: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}) in {color} color")

    def __str__(self):
        return f"Triangle: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3})"


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x, self.y, self.radius = x, y, radius

    def draw(self, color):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in {color} color")

    def __str__(self):
        return f"Circle: ({self.x}, {self.y}) with radius {self.radius}"
