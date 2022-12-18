import pygame
pygame.init()

width = 1000
height = 1000

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

def draw():
    for i in range(100, 1000, 100):
        pygame.draw.line(win, red,(i, 0), (i, 1000))
    for i in range(100, 1000, 100):
        pygame.draw.line(win, red,(0, i), (1000, i))

win = pygame.display.set_mode((width, height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))
    draw()
    pygame.display.update()