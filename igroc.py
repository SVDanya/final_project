import pygame
import Common

win = Common.win

class Player():
    def __init__(self):
        self.x = 0
        self.y = 0

    def update(self):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, 100, 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 100
            pygame.time.delay(200)
        if keys[pygame.K_DOWN]:
            self.y += 100
            pygame.time.delay(200)
        if keys[pygame.K_LEFT]:
            self.x -= 100
            pygame.time.delay(200)
        if keys[pygame.K_RIGHT]:
            self.x += 100
            pygame.time.delay(200)