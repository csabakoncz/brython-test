import typing
import browser
from browser import document
import math

from rstubs import Canvas, Context2D
from browser import document

from .vector import Vector, Line

number = typing.Union[int, float]

class PlotContext:
    def __init__(self, ctx: Context2D):
        self.ctx = ctx

    def __enter__(self) -> Context2D:
        self.ctx.save()
        self._configure_context()

        return self.ctx

    def _configure_context(self):
        raise Exception('Not implemented')

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.ctx.restore()


class TranslatedContext(PlotContext):
    def __init__(self, ctx: Context2D, w: number,
                 h: number):
        super().__init__(ctx)
        self.w = w
        self.h = h

    def _configure_context(self):
        self.ctx.translate(self.w / 2, self.h / 2)
        self.ctx.scale(1, -1)


class StyledContext(PlotContext):
    def __init__(self, ctx: Context2D, lineWidth: number,
                 strokeStyle: str):
        super().__init__(ctx)
        self.lineWidth = lineWidth
        self.strokeStyle = strokeStyle

    def _configure_context(self):
        self.ctx.lineWidth = self.lineWidth
        self.ctx.strokeStyle = self.strokeStyle


class Plot():
    canvas: Canvas

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.ctx = canvas.getContext("2d")

        w = canvas.width
        h = canvas.height

        # axes
        self.ctx.lineWidth = 1
        self.ctx.strokeStyle = "gray"
        self.line(Vector(0, -h / 2), Vector(0, h / 2))
        self.line(Vector(-w / 2, 0), Vector(w / 2, 0))

        self.ctx.lineWidth = 3
        self.ctx.strokeStyle = "black"

    def plot_context(self) -> PlotContext:
        return TranslatedContext(self.ctx, self.canvas.width,
                                 self.canvas.height)

    def clear(self):
        self.ctx.clearRect(0, 0, self.canvas.width, self.canvas.height)

    def circle(self, c: Vector, r: float):
        with self.plot_context() as ctx:
            ctx.beginPath()
            ctx.arc(c.x, c.y, r, 0, 2 * math.pi)
            ctx.stroke()

    def line(self, v1: Vector, v2: Vector):
        with self.plot_context() as ctx:
            ctx.beginPath()
            ctx.moveTo(v1.x, v1.y)
            ctx.lineTo(v2.x, v2.y)
            ctx.stroke()

    def triangle(self, v1: Vector, v2: Vector, v3: Vector):
        with self.plot_context() as ctx:
            ctx.beginPath()
            ctx.moveTo(v1.x, v1.y)
            ctx.lineTo(v2.x, v2.y)
            ctx.lineTo(v3.x, v3.y)
            ctx.lineTo(v1.x, v1.y)
            ctx.stroke()

    def style(self, lineWidth: number, strokeStyle: str) -> StyledContext:
        return StyledContext(self.ctx,
                             lineWidth=lineWidth,
                             strokeStyle=strokeStyle)

    def semiline(self, line: Line, length: number):
        with self.style(lineWidth=1, strokeStyle="gray") as ctx:
            self.line(line.start, line.start + line.direction * length)

    def demo(self):
        V1 = Vector(-100, 200)
        V2 = Vector(-300, -200)
        V3 = Vector(300, -200)
        self.triangle(V1, V2, V3)

        # bisector in V1:
        B1 = Line(V1, (V2 - V1).normalized() + (V3 - V1).normalized())
        self.semiline(B1, 500)

        # bisector in V2:
        B2 = Line(V2, (V1 - V2).normalized() + (V3 - V2).normalized())
        self.semiline(B2, 500)

        C = B1.intersection_with(B2)

        N = Line(C, (V2 - V1).normal_to())

        T = N.intersection_with(Line(V1, V2 - V1))

        r = (T - C).length()

        self.line(C, T)
        self.circle(C, r)

    @classmethod
    def DEMO(cls, canvasId: str):
        canvas: Canvas = document.getElementById(canvasId)
        p = Plot(canvas)
        p.demo()
