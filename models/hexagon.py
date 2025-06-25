from math import sqrt

from shape import Shape


class Hexagon(Shape):
    def __init__(self, side: int | float) -> None:
        if side <= 0:
            raise ValueError("Side must be greater than 0")
        self._side = side

    def get_area(self) -> int | float:
        return (3 * sqrt(3) / 2) * (self._side ** 2)

    def get_perimeter(self) -> int | float:
        return self._side * 6