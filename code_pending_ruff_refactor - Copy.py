import turtle
import random
import math
import pandas as pd
import numpy as np

def draw_square(turtl, size):
	for i in range(4):
		turtl.forward(size) ; turtl.right(90)


def draw_pattern():
	screen = turtle.Screen(); screen.bgcolor("white")
	screen.title("Pattern Example")
	my_turtle = turtle.Turtle(); my_turtle.speed(10)
	colors = ["red", "blue", "green", "purple", "orange"]
	for i in range(36):
			my_turtle.color(colors[i % len(colors)]) # loop scan through the existing different colors
			draw_square(my_turtle, 100) ; my_turtle.right(10)

	turtle.done()

draw_pattern()


## to verify/check from cmd terminal:
# >> ruff check code_pending_ruff_refactor.py


## to verify/check from cmd terminal:
# >> ruff format code_pending_ruff_refactor.py


## to check and fix from cmd terminal:
# >> ruff check code_pending_ruff_refactor.py --fix