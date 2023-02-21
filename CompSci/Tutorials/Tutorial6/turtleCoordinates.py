import turtle


x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))


t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-50, -25)
t.pendown()


for i in range(2):
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)


t.penup()
t.goto(x, y)
t.dot(5)


if abs(x) <= 50 and abs(y) <= 25:
    message = "The point is inside the rectangle."
else:
    message = "The point is outside the rectangle."


t.penup()
t.goto(0, -40)
t.write(f"Point: ({x}, {y})\n{message}", align="center", font=("Arial", 12, "normal"))


turtle.done()
