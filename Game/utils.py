from turtle import *

__all__ = [
    "TextTurtle",
    "GIFTurtle",
]

def TextTurtle(x, y, color):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(x, y)
    t.speed(0)
    t.color(color)
    return t

def GIFTurtle(fname):
    t = Turtle(fname + ".gif")
    t.speed(0)
    t.up()
    return t
