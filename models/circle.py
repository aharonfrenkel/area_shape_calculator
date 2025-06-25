from math import pi

from shape import Shape


class Circle(Shape):
    def __init__(self, radius: int | float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
        self._radius = radius

    def get_area(self) -> int | float:
        return pi * self._radius * self._radius

    def get_perimeter(self) -> int | float:
        return self._radius * 2 * pi