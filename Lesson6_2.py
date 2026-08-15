import pygame
from pygame.locals import *
from time import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
playerx = 200
playery = 200

keys = [False, False, False, False]  # UP, LEFT, DOWN, RUGHT

player = pygame.image.load("character.png")
bg = pygame.image.load("background.png")

while playery < 600:
    screen.blit(bg, (0, 0))
    screen.blit(player, (playerx, playery))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:  # key press
            if event.key == K_UP:
                keys[0] = True

            elif event.key == K_LEFT:
                keys[1] = True

            elif event.key == K_DOWN:
                keys[2] = True

            elif event.key == K_RIGHT:
                keys[3] = True

        if event.type == pygame.KEYUP:  # key release
            if event.key == pygame.K_UP:
                keys[0] = False

            elif event.key == pygame.K_LEFT:
                keys[1] = False

            elif event.key == pygame.K_DOWN:
                keys[2] = False

            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        if playery > 0:
            playery -= 7

    elif keys[2]:
        if playery < 536:
            playery += 7

    if keys[1]:
        if playerx > 0:
            playerx -= 2

    elif keys[3]:
        if playerx < 536:
            playerx += 2

    playery += 5

    sleep(0.05)

print("Game Over!")
