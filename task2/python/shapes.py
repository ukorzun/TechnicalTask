from abc import abstractmethod


class Engine2D:

    def __init__(self):
        self.canvas = []
        self.current_color = "black"

    def add_shape(self, shape):
        self.canvas.append(shape)

    def set_color(self, color):
        print(f"Setting color to: {color}")
        self.current_color = color

    def draw(self):
        for shape in self.canvas:
            shape.draw(self.current_color)
        self.canvas.clear()


class Shape:

    @abstractmethod
    def draw(self, color):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, color):
        print(
            f"Drawing Rectangle: ({self.x}, {self.y}) with width {self.width} and height {self.height} in {color} color")


class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.x3, self.y3 = x3, y3

    def draw(self, color):
        print(
            f"Drawing Triangle: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3}) in {color} color")


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, color):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius} in {color} color")
