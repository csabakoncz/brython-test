import typing
from .context2d import Context2D


class Canvas():
    width: int
    height: int
    def getContext(self, kind: typing.Literal['2d']) -> Context2D:
        pass