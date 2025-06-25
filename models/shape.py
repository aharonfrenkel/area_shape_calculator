from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self) -> int | float:
        pass

    @abstractmethod
    def get_perimeter(self) -> int | float:
        pass

    def _get_attrs(self) -> str:
        attrs = (f"{key.lstrip('_')}={value!r}" for key, value in self.__dict__.items())
        return f"{', '.join(attrs)}"

    def _get_properties(self) -> str:
        properties = (f"{name.lstrip('_')}={getattr(self, name)}" for name in dir(self)
              if isinstance(getattr(type(self), name, None), property))
        return f"{', '.join(properties)}"

    def __str__(self) -> str:
        attrs = self._get_attrs()
        props = self._get_properties()
        if props:
            return f"({attrs}, {props})"
        return f"({attrs})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._get_attrs()})"