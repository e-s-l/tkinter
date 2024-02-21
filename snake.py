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

class snake:

#define sole method, initialize

#using methds from tkinter: coordinates, canvas, create_rectangle, squares?

    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

###############

#using randint from random to place food somewhere

class food:

    def __init__(self):

        #
        x = random.randint(0,(WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0,(HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        #
        self.coordinates = [x,y]

        #change this to rectangle
        canvas.create_oval(x,y,(x+SPACE_SIZE),(y+SPACE_SIZE),fill=FOOD_COLOR,tag='food')

################
#FUNCTIONS:
################

def next_turn(snake, food):

    x, y = snake.coordinates[0,0]

    if direction=="UP":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right"
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_recantagle(x,y,(x+SPACE_SIZE),(y+SPACE_SIZE), fill = SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score +=1
        label.config(text='Points{}'.format(score))
        canvas.delete('food')
        food = food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)
        
########################

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

############################

def check_collisions(snake):

    x,y = snake.coordinates[0]

    if x<0 or x>=WIDTH:
        return True
    elif y<0 or y>=HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True

    return False

#########################

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER",fill="red",tag="gameover")

#thats the end of function definitions
#########################