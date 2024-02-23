#
#python tkinter snake game... 
#based off web results from quick google search
#practice and experience with tkinter
#

#IMPORTS
from tkinter import *
import random

#
import sys
import os
######################

#INITIALISATION:
#(capitalise constants.)

#GAME SCREEN DIMENSIONS:
WIDTH=800                   #WIDTH = window.winfo_width ??
HEIGHT=800
SPACE_SIZE=20

#SNAKE INITIALISATION:
BODY_SIZE=2
SPEED = 100

#COLOURS:
SNAKE_COLOR='#551A8B'#'#00FF00'
FOOD_COLOR='#0000EE'#FFFFFF'
BACKGROUND_COLOR='#000000'

####################

#define class for the snake object:

class Snake:
#define sole method, initialize

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

class Food:

    def __init__(self):

        #
        x = random.randint(0,(WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0,(HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE

        #
        self.coordinates = [x,y]

        #change this to rectangle
        canvas.create_rectangle(x,y,(x+SPACE_SIZE),(y+SPACE_SIZE),fill=FOOD_COLOR,tag='food')

################
#FUNCTIONS:
################

def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction=="up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(x,y,(x+SPACE_SIZE),(y+SPACE_SIZE), fill = SNAKE_COLOR)

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score +=1
        label.config(text='Points{}'.format(score))
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        print("collision detected...")
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

    #if snake exceeds the boundaries of its domain
    if x<0 or x>=WIDTH:
        return True
    elif y<0 or y>=HEIGHT:
        return True

    #self-interaction
    for body_part in snake.coordinates[1:]:
        if x==body_part[0] and y==body_part[1]:
            return True

    return False

#########################

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=('consolas',70),text="GAME OVER",fill="red",tag="gameover")
    print("it's game over man")

#########################

def Restart():

    #
    python = sys.executable
    os.execl(python, python, * sys.argv)
   


###########################

score = 0
direction='down'
window = Tk()

window.title('Tk Snake(python)')

label = Label(window, text="Points:"+" "+"{}".format(score),font=('consolas,20'))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)

canvas.pack(fill="both", expand=True) #how to adjust game boundaries based on canva boundaries... 

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")


#COMMANDS
window.bind('<Left>',lambda event: change_direction('left'))
window.bind('<Right>',lambda event: change_direction('right'))
window.bind('<Up>',lambda event: change_direction('up'))
window.bind('<Down>',lambda event: change_direction('down'))
#hot keys to quit r restart
window.bind('<R>',lambda event: Restart())
window.bind('<Q>',lambda event: sys.exit())
#Other Modes
window.bind('<E>',lambda event: EasyMode())
window.bind('<H>',lambda event: HardMode())

######
snake = Snake()
food = Food()

next_turn(snake,food)
####
window.mainloop()

#############################


#snakeTheGame()