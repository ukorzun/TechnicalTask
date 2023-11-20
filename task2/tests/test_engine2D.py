import unittest
from io import StringIO
import re
from contextlib import redirect_stdout
from task2.python.shapes import Engine2D, Circle, Triangle, Rectangle


class TestEngine2D(unittest.TestCase):

    def setUp(self):
        self.engine = Engine2D()

    def assertShapeOutput(self, shape, color, expected_output):
        with StringIO() as buf, redirect_stdout(buf):
            self.engine.draw()
            output = buf.getvalue()
        pattern = re.compile(re.escape(expected_output).replace(r'\ ', '.*?'))
        self.assertRegex(output, pattern)

    def assertOutputEqual(self, expected_output, function, *args, **kwargs):
        with StringIO() as buf, redirect_stdout(buf):
            function(*args, **kwargs)
            output = buf.getvalue()
        self.assertEqual(output, expected_output, f"Output mismatch:\nExpected: {expected_output}\nActual: {output}")

    def test_unsupported_color(self):
        unsupported_color = "purple"
        self.engine.set_color(unsupported_color)
        self.assertEqual(self.engine.current_color, "black",
                         f"Setting unsupported color '{unsupported_color}' should keep the current color, "
                         f"but got '{self.engine.current_color}' instead of 'black'")

    def test_initialization(self):
        self.assertEqual(self.engine.canvas, [])
        self.assertEqual(self.engine.current_color, "black")

    def test_add_shape(self):
        circle = Circle(0, 0, 5)
        self.engine.add_shape(circle)
        self.assertIn(circle, self.engine.canvas)

    def test_set_color(self):
        self.engine.set_color("red")
        self.assertEqual(self.engine.current_color, "red")

    def test_draw_single_circle(self):
        circle = Circle(0, 0, 5)
        self.engine.add_shape(circle)
        self.assertShapeOutput(circle, "black", "Drawing Circle: (0, 0) with radius 5 in black color")
        self.assertEqual(self.engine.canvas, [])

    def test_draw_multiple_shapes(self):
        circle = Circle(0, 0, 5)
        triangle = Triangle(1, 2, 3, 4, 5, 6)
        rectangle = Rectangle(2, 2, 4, 3)
        self.engine.add_shape(circle)
        self.engine.set_color("red")
        self.engine.add_shape(triangle)
        self.engine.add_shape(rectangle)

        expected_output = (
            "Drawing Circle: (0, 0) with radius 5 in red color\n"
            "Drawing Triangle: (1, 2), (3, 4), (5, 6) in red color\n"
            "Drawing Rectangle: (2, 2) with width 4 and height 3 in red color\n"
        )

        self.assertOutputEqual(expected_output, self.engine.draw)
        self.assertEqual(self.engine.canvas, [])

    def test_draw_no_shapes(self):
        self.assertOutputEqual("", self.engine.draw)
        self.assertEqual(self.engine.canvas, [])


class TestShapes(unittest.TestCase):

    def assertShapeOutput(self, shape, color, expected_output):
        with StringIO() as buf, redirect_stdout(buf):
            shape.draw(color)
            output = buf.getvalue()
        pattern = re.compile(re.escape(expected_output).replace(r'\ ', '.*?'))
        self.assertRegex(output, pattern, f"Output mismatch: {expected_output} != {output}")

    def test_circle_initialization(self):
        circle = Circle(1, 2, 3)
        self.assertEqual((circle.x, circle.y, circle.radius), (1, 2, 3))

    def test_triangle_initialization(self):
        triangle = Triangle(1, 2, 3, 4, 5, 6)
        self.assertEqual((triangle.x1, triangle.y1, triangle.x2, triangle.y2, triangle.x3, triangle.y3),
                         (1, 2, 3, 4, 5, 6))

    def test_draw_circle(self):
        circle = Circle(0, 0, 5)
        self.assertShapeOutput(circle, "blue", "Drawing Circle: (0, 0) with radius 5 in blue color")

    def test_draw_triangle(self):
        triangle = Triangle(1, 2, 3, 4, 5, 6)
        self.assertShapeOutput(triangle, "green", "Drawing Triangle")


if __name__ == '__main__':
    unittest.main()
