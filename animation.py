import turtle
import colorsys

# Set up the screen window
window = turtle.Screen()
window.bgcolor("black")

# Create two visible turtle objects
t1 = turtle.Turtle()
t1.shapesize(3)
t1.color("#ff0000")
t1.pensize(15)

t2 = turtle.Turtle()
t2.shapesize(3)
t2.color("#ff0000")
t2.pensize(15)

iterations = 360

def click_handler(x, y):
    t1.clear()
    t2.clear()
    t1.pendown()
    t2.pendown()
    t1.forward(10)
    t1.teleport(0, 0)
    t2.teleport(10, 0)
    t1.speed(0)
    t2.speed(0)
    for i in range(iterations):
        hue = i / iterations
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t1.color(rgb)
        t2.color(rgb)
        step = i / 3
        t1.forward(step)
        t1.right(15)
        t2.forward(step)
        t2.right(15)

def clear():
    t1.clear()
    t2.clear()
    t1.penup()
    t2.penup()
    t1.home()
    t2.home()

# Bind the same click handler to both turtles so clicking either triggers both
t1.onclick(click_handler)
t2.onclick(click_handler)
# Click space after simulation has finished to reset
window.onkey(clear, "space")
window.listen()

window.mainloop()
