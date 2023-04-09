#!/usr/bin/env python3
#Created by PepeBigotes, with major assistance of OpenAI's ChatGPT

import pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Set up the display window
size = (210, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mod Menu Template")

# Define the font
font = pygame.font.SysFont('dejavusans', 25, True, False)

# Define the button class
class Button:
    def __init__(self, text, x, y, width, height, function):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = function
        self.hovered = False

    def draw(self, surface):
        if self.hovered:
            pygame.draw.rect(surface, GRAY, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, BLACK)
        text_rect = text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        surface.blit(text, text_rect)

    def update(self, mouse_pos):
        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            self.hovered = True
        else:
            self.hovered = False

    def execute(self):
        self.function()

class Title:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface):
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        surface.blit(text, text_rect)


# Define the functions to be executed by the buttons
def function1():
    print("Function 1 executed")

def function2():
    print("Function 2 executed")

def function3():
    print("Function 3 executed")

def function4():
    print("Function 4 executed")

def function5():
    print("Function 5 executed")

# Create the buttons
title = Title("Epic Mod Menu", 5, 0, 200, 50)
button1 = Button("Button 1", 5, 50, 200, 45, function1)
button2 = Button("Button 2", 5, 100, 200, 45, function2)
button3 = Button("Button 3", 5, 150, 200, 45, function3)
button4 = Button("Button 4", 5, 200, 200, 45, function4)
button5 = Button("Button 5", 5, 250, 200, 45, function5)

# Add the buttons to a list
buttons = [button1, button2, button3, button4, button5]

# Loop until the user clicks the close button
done = False

# Main game loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the user clicked on a button
            for button in buttons:
                if button.hovered:
                    button.execute()

    # --- Update the button states
    for button in buttons:
        button.update(pygame.mouse.get_pos())

    # --- Drawing code should go here
    screen.fill(BLACK)

    # Draw the buttons
    for button in buttons:
        button.draw(screen)
    title.draw(screen)

    # --- Go ahead and update the screen
    pygame.display.flip()

# Close the window and quit.
pygame.quit()
