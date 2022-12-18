import pygame
win =

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.image.load('main.py')
        #self.image = self.image.convert()
        #colorkey = self.image.get_at((0, 0))
        #self.image.set_colorkey(colorkey)
        #self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

    def draw(self):
        pygame.draw.rect(win, red, (51, 0, 50, 50), 2)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.top -= 5
        if keys[pygame.K_DOWN]:
            self.rect.top += 5
        if keys[pygame.K_LEFT]:
            self.rect.left -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.left += 5

all_sprites = pygame.sprite.Group()
