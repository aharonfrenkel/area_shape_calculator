from math import sqrt

from shape import Shape


class RightTriangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")
        self._width = width
        self._height = height

    @property
    def hypotenuse(self) -> float:
        return sqrt(self._width ** 2 + self._height ** 2)

    def get_area(self) -> int | float:
        return self._width * self._height / 2

    def get_perimeter(self) -> int | float:
        return self._width + self._height + self.hypotenuse