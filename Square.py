import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Moving Square")

clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 200)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)

        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)

        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
