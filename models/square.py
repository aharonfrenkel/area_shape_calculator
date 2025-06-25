from shape import Shape


class Square(Shape):
    def __init__(self, side: int | float) -> None:
        if side <= 0:
            raise ValueError("Side must be greater than 0")
        self._side = side

    def get_area(self) -> int | float:
        return self._side ** 2

    def get_perimeter(self) -> int | float:
        return 4 * self._side