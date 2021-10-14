class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.height = height
        self.width = width
        self.color = color
        self.y = y
        self.x = x

    def draw(self, canvas):
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color