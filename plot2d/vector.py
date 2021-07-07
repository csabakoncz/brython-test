import math
import typing


class Vector:
    x: float
    y: float

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __rmul__(self, other: typing.Union[int, float]) -> 'Vector':
        return Vector(self.x * other, self.y * other)

    @typing.overload
    def __mul__(self, other: typing.Union[int, float]) -> 'Vector':
        pass

    @typing.overload
    def __mul__(self, other: 'Vector') -> float:
        pass

    def __mul__(self, other: typing.Union[int, float, 'Vector']):
        if isinstance(other, (float, int)):
            return self.mul(other)
        elif isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y

    def mul(self, other: typing.Union[int, float]) -> 'Vector':
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other: typing.Union[int, float]) -> 'Vector':
        return self.mul(1.0 / other)

    def normalized(self) -> 'Vector':
        return self.mul(1.0 / self.length())

    def normal_to(self) -> 'Vector':
        return Vector(self.y, -self.x)

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x, self.y)


class Line:
    def __init__(self, start: Vector, direction: Vector):
        """
        Create a line through the given point and having the direction
        of the second argument.
        :param start:
        :param direction: vector showing the direction (will be normalized)
        """
        self.start = start
        self.direction = direction.normalized()

    def intersection_with(self, other: 'Line') -> Vector:
        v10 = other.start
        v1d = other.direction
        v20 = self.start
        v2d = self.direction

        v1dn = v1d.normal_to()

        u = ((v10 - v20) * v1dn) / (v2d * v1dn)

        return self.start + u * self.direction

    def __repr__(self):
        return 'Line( start=%s , direction=%s )' % (self.start, self.direction)
