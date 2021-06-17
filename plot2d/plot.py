import browser
from browser import document
import math

from rstubs import Canvas
from browser import document

from .vector import Vector,Line


class Plot():
    canvas: Canvas

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.ctx = canvas.getContext("2d")
        # self.ctx.translate(0, canvas.height)
        # self.ctx.scale(1, -1)
        self.ctx.lineWidth = 3
        self.ctx.strokeStyle = "black"

    def clear(self):
        self.ctx.clearRect(0, 0, self.canvas.width, self.canvas.height)

    def circle(self, c: Vector, r: float):
        ctx = self.ctx

        ctx.beginPath()
        ctx.arc(c.x, c.y, r, 0, 2 * math.pi)
        ctx.stroke()

    def line(self, v1: Vector, v2: Vector):
        ctx = self.ctx

        ctx.beginPath()
        ctx.moveTo(v1.x, v1.y)
        ctx.lineTo(v2.x, v2.y)
        ctx.stroke()

    def triangle(self, v1: Vector, v2: Vector, v3: Vector):
        ctx = self.ctx

        ctx.beginPath()
        ctx.moveTo(v1.x, v1.y)
        ctx.lineTo(v2.x, v2.y)
        ctx.lineTo(v3.x, v3.y)
        ctx.lineTo(v1.x, v1.y)
        ctx.stroke()

    def demo(self):
        V1=Vector(300,100)
        V2=Vector(100,400)
        V3=Vector(700,400)
        self.triangle(V1,V2,V3)

        # bisector in V1:
        B1 = Line(V1,(V2-V1).normalized()+(V3-V1).normalized())

        # bisector in V2:
        B2 = Line(V2,(V1-V2).normalized()+(V3-V2).normalized())

        C = B1.intersection_with(B2)

        N = Line(C,(V2-V1).normal_to())

        T = N.intersection_with(Line(V1,V2-V1))

        r = (T - C).length()

        self.line(C,T)
        self.circle(C,r)

    @classmethod
    def DEMO(cls, canvasId: str):
        canvas: Canvas = document.getElementById(canvasId)
        p = Plot(canvas)
        p.clear()
        p.demo()




