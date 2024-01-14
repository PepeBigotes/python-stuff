#!/usr/bin/env python3
#Created by PepeBigotes

from random import randint
import os
from time import sleep
from keyboard import is_pressed, wait


# Output Vars
FULL_CHAR = '#'
EMPTY_CHAR = '.'
blink_fill = True


# System Vars
score = 0
snake_lenght = 3

TICK_SPEED = .2
TICKS_PER_MTICK = 3
ticks_till_mtick = 0

APPLES_TO_SPAWN = 1
active_apples = 0

head_y = None
head_x = None

class Pixel():
    global snake_lenght
    def __init__(self, y, x):
        self.type = 'empty'
        self.display = 'empty'
        self.mt_from_head = -1
        self.y = y
        self.x = x
    def set(self, t):
        if t == 'head':
            global head_y, head_x
            head_y = self.y
            head_x = self.x
            self.type = 'head'
            self.display = 'blink'
            self.mt_from_head = 0
        elif t == 'wall':
            self.type = 'wall'
            self.display = 'full'
            self.mt_from_head = -1
        elif t == 'apple':
            self.type = 'apple'
            self.display = 'blink'
        elif t == 'tail':
            self.type = 'tail'
            self.display = 'full'
        elif t == 'empty':
            self.type = 'empty'
            self.display = 'empty'
    def update_tail(self):
        if self.type == 'wall' or self.mt_from_head < 0: return
        global snake_lenght
        self.mt_from_head += 1
        if self.mt_from_head <= snake_lenght: self.set('tail')
        else: self.set('empty')
            
matrix = []
DIRECTIONS = {
    'up': 1,
    'down': 1,
    'left': -1,
    'right': -1
}


# Input Vars
direction = None
new_direction = None
i_up = False
i_left = False
i_down = False
i_right = False

def update_tail():
    for y in matrix:
        for x in y:
            x.update_tail()
def find(t):
    pixels = []
    for y in matrix:
        for x in y:
            if x.type == t: pixels.append(x)
    if not pixels: return []
    return pixels

def spawn(t):
    global matrix
    empty_pixels = find('empty')
    if not empty_pixels: return None
    empty_pixels[randint(0, len(empty_pixels))].set(t)

def init():
    global matrix
    matrix = [[Pixel(y,x) for x in range(17)] for y in range(17)]
    for y in matrix:
        y[0].set('wall')
        y[-1].set('wall')
        if y == matrix[0] or y == matrix[-1]:
            for x in y:
                x.set('wall')
    spawn('head')
    

def handle_system():
    global matrix, active_apples, snake_lenght, score, ticks_till_mtick, direction, new_direction
    active_apples = len(find('apple'))
    if active_apples < APPLES_TO_SPAWN: spawn('apple')
    if new_direction and direction != None: direction = new_direction
    if new_direction and not DIRECTIONS.get(new_direction, 1) * DIRECTIONS.get(direction, 1) == 1: direction = new_direction # Cannot turn 180, only 90 
    if ticks_till_mtick == 0:
        ticks_till_mtick = TICKS_PER_MTICK

        if not direction: next_pixel = matrix[head_y][head_x].set('head')
        else:
            if direction == 'up': next_pixel = matrix[head_y-1][head_x]
            elif direction == 'down': next_pixel = matrix[head_y+1][head_x]
            elif direction == 'left': next_pixel = matrix[head_y][head_x-1]
            elif direction == 'right': next_pixel = matrix[head_y][head_x+1]
            if next_pixel.type == 'wall' or next_pixel.type == 'tail':
                print("=GAME OVER=")
                exit()
            else:
                if next_pixel.type == 'apple':
                    snake_lenght += 1
                    score += 1
                update_tail()
                next_pixel.set('head')
        
    else: ticks_till_mtick -= 1
    


def handle_input():
    global i_up, i_left, i_down, i_right, direction, new_direction
    i_up = (is_pressed('w') or is_pressed('up'))
    i_left = (is_pressed('a') or is_pressed('left'))
    i_down = (is_pressed('s') or is_pressed('down'))
    i_right = (is_pressed('d') or is_pressed('right'))
    checksum = 0
    if i_up: checksum += 1
    if i_left: checksum += 1
    if i_down: checksum += 1
    if i_right: checksum += 1
    if checksum > 1: return
    new_direction = None
    if i_up: new_direction = 'up'
    elif i_left: new_direction = 'left'
    elif i_down: new_direction = 'down'
    elif i_right: new_direction = 'right'
    
    
    

def handle_output():
    if is_pressed('esc'):
        print("Game paused, press ESC again to continue")
        sleep(1)
        wait('esc')
    global score, direction
    os.system('cls' if os.name=='nt' else 'clear') # Clear terminal
    global matrix, blink_fill
    blink_fill = not blink_fill
    print(f"Score: {score}")
    print(f"Dir: {direction}")
    for y in matrix:
        for x in y:
            if x.display == 'full': print(FULL_CHAR, end='')
            elif x.display == 'blink' and blink_fill: print(FULL_CHAR, end='')
            else: print(EMPTY_CHAR, end='')
        print("")
    


try:
    init()
    while True:
        sleep(TICK_SPEED)
        handle_input()
        handle_system()
        handle_output()
except KeyboardInterrupt:
    print("KeyboardInterrupt")