import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fathers Day Card")

img = pygame.image.load("backgroundone.jpg")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display_surface.fill((255, 255, 255))
    display_surface.blit(image, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)

    img2 = pygame.image.load("backgroundtwo.jpg")
    image2 = pygame.transform.scale(img2, (WIDTH, HEIGHT))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image2, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)

    img3 = pygame.image.load("backgroundthree.jpg")
    image3 = pygame.transform.scale(img3, (WIDTH, HEIGHT))
    display_surface.fill((255, 255, 255))
    display_surface.blit(image3, (0, 0))
    pygame.display.update()
    pygame.time.delay(2000)
