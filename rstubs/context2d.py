class Context2D():

    lineWidth: float
    strokeStyle: str
    fillStyle: str

    def translate(self, x: float, y: float):
        pass

    def scale(self, x: float, y: float):
        pass

    def beginPath(self):
        pass

    def stroke(self):
        pass

    def moveTo(self, x: float, y: float):
        pass

    def lineTo(self, x: float, y: float):
        pass

    def arc(self, cx: float, cy: float, startRad: float, endRad: float, counterclockwise=False):
        pass

    def clearRect(self, x1: float, y1: float, width: float, height: float):
        pass

    def save(self):
        pass

    def restore(self):
        pass
