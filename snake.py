# snake.py

import tkinter as tk
import random
import sys
import os


SPACE_SIZE = 20
BODY_SIZE = 2
WIDTH=800                   
HEIGHT=800
#

SNAKE_COLOR = '#00FF00' #'#551A8B'
FOOD_COLOR = '#0000EE'
BACKGROUND_COLOR = '#000000'
direction = 'down'
score = 0
speed = 75

#globals

infinteMode = False

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.paused = False

        self.title('Snake')
        self.score_label = tk.Label(self, text="Points: {}".format(score), font=('consolas', 20))
        self.score_label.pack()
        #
        self.bind('<Left>', lambda event: self.change_direction('left'))
        self.bind('<Right>', lambda event: self.change_direction('right'))
        self.bind('<Up>', lambda event: self.change_direction('up'))
        self.bind('<Down>', lambda event: self.change_direction('down'))
        self.bind('<R>', lambda event: self.restart())
        self.bind('<Q>', lambda event: sys.exit())
        self.bind('<P>', lambda event: self.toggle_pause())
        self.bind('<I>', lambda event: self.toggle_infinite_mode())
        self.bind('1', lambda event: self.halfSpeed())
        self.bind('2', lambda event: self.doubleSpeed())

        #
        self.canvas = tk.Canvas(self, bg=BACKGROUND_COLOR, height=HEIGHT, width=WIDTH)
        self.canvas.pack(expand=True)
        #
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.next_turn()
 

    def halfSpeed(self):
        global speed
        speed = int(speed*2)
        print('speed = {}'.format(speed))

    def doubleSpeed(self):
        global speed
        speed = int(speed/2)
        if speed <= 0.0:
            speed = 1
        print('speed = {}'.format(speed))

    def toggle_infinite_mode(self):
        global infinteMode
        global SNAKE_COLOR
        if infinteMode:
            infinteMode = False
            SNAKE_COLOR = '#00FF00'
        else:
            infinteMode = True
            SNAKE_COLOR = '#551A8B'
            print('No Walls!')

    def toggle_pause(self):
        self.paused = not self.paused  # Toggle pause status
        if self.paused:
            self.canvas.create_text(WIDTH/2, (HEIGHT/2), font=('consolas', 40), text="PAUSED", fill="white", tag="paused")
            self.canvas.create_text(WIDTH/2, (HEIGHT/4), font=('consolas', 20), text=" [P]: Pause \t [Q]: Quit \n  \n [R]: Restart \t [I]: Infinite Mode \n \n [1]: Slow down  [2]: Speed up ", fill="white", tag="paused")
        else:
            self.canvas.delete("paused")
            self.next_turn()  # Resume the game if it was paused

    def next_turn(self):
        if not self.paused:  # Check if the game is paused
            global direction, score
            x, y = self.snake.coordinates[0]
            if direction == "up":
                y -= SPACE_SIZE
            elif direction == "down":
                y += SPACE_SIZE
            elif direction == "left":
                x -= SPACE_SIZE
            elif direction == "right":
                x += SPACE_SIZE
            self.snake.move_snake(x, y)
            if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
                score += 1
                self.score_label.config(text='Points: {}'.format(score))
                self.food.reload()
            else:
                self.snake.remove_tail()
            if self.check_collisions():
                self.game_over()
            else:
                self.after(speed, self.next_turn)

    def change_direction(self, new_direction):
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

    def check_collisions(self):
        global infinteMode
        x, y = self.snake.coordinates[0]
        if not infinteMode:
            if x < 0 or x >= WIDTH:
                return True
            elif y < 0 or y >= HEIGHT:
                return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(WIDTH / 2, HEIGHT / 2, font=('consolas', 70), text="GAME OVER", fill="red")

    def restart(self):
        program = sys.executable
        os.execl(program, program, *sys.argv)


class Snake:
    def __init__(self, canvas):
        self.canvas = canvas  # Store the canvas object
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        for i in range(0, BODY_SIZE):
            self.coordinates.append([0, 0])
        for x, y in self.coordinates:
            square = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
            self.squares.append(square)

    def move_snake(self, x, y):
        global infinteMode
        if infinteMode:
            if x < 0:
                x = WIDTH - SPACE_SIZE
            elif x > WIDTH:
                x = 0 #+ (x - WIDTH)
            elif y < 0:
                y = HEIGHT - SPACE_SIZE
            elif y > HEIGHT:
                y = 0 #+ (y - HEIGHT)


        self.coordinates.insert(0, (x, y))
        self.squares.insert(0, self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR))


    def remove_tail(self):
        self.canvas.delete(self.squares[-1])
        del self.squares[-1]
        del self.coordinates[-1]


class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        x = random.randint(0, (WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.rectangle = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')

    def reload(self):
        self.canvas.delete(self.rectangle)
        x = random.randint(0, (WIDTH/ SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT/ SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        self.rectangle = self.canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')



if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()