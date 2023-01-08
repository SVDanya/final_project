import random

import pygame
import igroc
import Common
pygame.init()
game_over = False

win = Common.win

width = 1000
height = 1000

player = igroc.Player()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
FPS = 60
clock = pygame.time.Clock()
def draw():
    for i in range(100, 1000, 100):
        pygame.draw.line(win, red,(i, 0), (i, 1000))
    for i in range(100, 1000, 100):
        pygame.draw.line(win, red,(0, i), (1000, i))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))


    pygame.draw.rect(win, (255, 0, 0), (100, 200, 100, 100))
    player.update()
    draw()
    pygame.display.update()
    clock.tick(FPS)