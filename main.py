import turtle
import keyboard

t = turtle.Turtle()
t.speed(200000)

while  True:
    keyboard.add_hotkey("w", lambda: t.forward(10))
    keyboard.add_hotkey("s", lambda: t.backward(10))
    keyboard.add_hotkey("a", lambda: t.left(90))
    keyboard.add_hotkey("d", lambda: t.right(90))

    turtle.exitonclick()