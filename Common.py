import igroc
import random
import pygame
dis_width = 1000
dis_height = 600
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

foodx = round(random.randrange(0, dis_width - igroc.snake_block) / 20.0) * 20.0
foody = round(random.randrange(0, dis_height - igroc.snake_block) / 20.0) * 20.0

game_over = True
game_close = False

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()