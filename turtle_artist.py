# Author: Layla ibrahim
# nov 3 2025



import turtle
window = turtle.Screen()
window.bgcolor("white")
turtle = turtle.Turtle()

# allow turtle to use 0–255 color values
# turtle.colormode(255)

colors = {
    "gold": "#ffd700",
    "blue": "#0000ff",
    "red": "#ff0000"
}

# first star - gold
turtle.color(colors["gold"])  # gold
for i in range(5):
    turtle.forward(100)
    turtle.right(144)


# move turtle without drawing
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

# second star - blue
turtle.color(colors["blue"])  # blue
for i in range(5):
    turtle.forward(100)
    turtle.right(144)

# move again
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()

# third star - red
turtle.color(colors["red"])  # red
for i in range(5):
    turtle.forward(100)
    turtle.right(144)

window.exitonclick()
