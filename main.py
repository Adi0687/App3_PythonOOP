from canvas import Canvas
from shapes import Square, Rectangle

# Get Canvas Size
canvas_width = int(input("Enter Canvas Width: "))
canvas_height = int(input("Enter Canvas Height: "))

# Canvas Color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter a color (black or white): ")

surface = Canvas(width=canvas_width, height=canvas_height, color=[colors[canvas_color]])

while True:
    shape = input("What would you like to draw (Square or rectangle)? If not please enter quit:  ")
    if shape.lower() == "square":
        # I just used the values directly instead of asking the user! Save time, Haha
        sq = Square(x=40, y=50, side=300, color=[0, 0, 0])
        sq.draw(canvas=surface)
    elif shape.lower() == "rectangle":
        # I just used the values directly instead of asking the user! Save time, Haha
        rec = Rectangle(x=400, y=500, width=300, height=400, color=[80, 90, 100])
        rec.draw(canvas=surface)
    else:
        break

surface.make('canvas.png')
