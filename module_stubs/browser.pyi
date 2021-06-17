"""
Does this work like a doctsring?
"""
from typing import Any, Callable, TypeVar

aio: Any

class Element:
    pass

class Context2D:
    pass

class Canvas(Element):
    def getContext(self, kind: str)->Context2D:
        pass


T = TypeVar('T')

class Document:
    def getElementById(self, id: str)->T:
        pass

""" Hope I can provide some useful stuff here
"""
document: Document
"Or like this?"

html: Any

IntervalId = int


class Timer:
    def set_interval(self, callback: Callable[[], None],
                     interval: int) -> IntervalId:
        pass

    def clear_interval(self, intervalId: IntervalId) -> None:
        pass


timer = Timer()


def alert(msg: str):
    "Browser alert"
    pass


def getDocument() -> Any:
    'hope it works'
    pass


def getDocument2():
    "where do I put the docstring?"
    return document
