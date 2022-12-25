import pygame
import Common

win = Common.win

class Player():

    def __int__(self):
        self.x = 0
        self.y = 0

    def update(self):
        pygame.draw.rect(win, (0, 255, 0), (0, 0, 100, 100))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= 5
        if keys[pygame.K_DOWN]:
            self.y += 5
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5

