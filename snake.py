import pygame
from pygame import time
import random

pygame.init()

# Define constants
#well colors first 
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
block_size = 20
#screen params
screen_width = 600
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PySnake')
clock = pygame.time.Clock()

# Function to display messages
def message(msg, color):
    font_style = pygame.font.SysFont("bahnschrift", 25)
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2
    x1_change = 0
    y1_change = 0

    # Snake body
    snake_List = []
    Length_of_snake = 1.2

    # Food position
    foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        # Update snake's head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # If snake is too long, remove the tail
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # If snake runs into itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        screen.fill(black)
        draw_snake(block_size, snake_List)
        pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])

        # Check if the snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
            Length_of_snake += 1

        pygame.display.update()

        clock.tick(5)  # Snake speed (FPS)

    pygame.quit()
    quit()

# Start the game
gameLoop()
