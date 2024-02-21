#
#python tkinter snake game... 
#based off web results from quick google search
#practice and experience with tkinter
#

#IMPORTS
from tkinter import *
import random

######################

#INITIALISATION:
#(capitalise constants.)

#GAME SCREEN DIMENSIONS:
WIDTH=500
HEIGHT=500
SPACE_SIZE=20

#SNAKE INITIALISATION:
BODY_SIZE=2
SPEED = 200

#COLOURS:
SNAKE_COLOR='#00FF00'
FOOD_COLOR='#FFFFFF'
BACKGROUND_COLOR='#000000'

####################

#define class for the snake object:

class snake

#define sole method, initialize

#using methds from tkinter: coordinates, canvas, create_rectangle, squares

    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE, tag="snake")
            self.squares.append(square)

