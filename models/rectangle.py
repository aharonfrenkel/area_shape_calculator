from shape import Shape


class Rectangle(Shape):
    def __init__(self, width: int | float, height: int | float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be greater than 0")
        self._width = width
        self._height = height

    def get_area(self) -> int | float:
        return self._width * self._height

    def get_perimeter(self) -> int | float:
        return 2 * (self._width + self._height)