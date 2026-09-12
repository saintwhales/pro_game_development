import pygame
from pygame.locals import *
from time import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
characterx = 200
charactery = 200

keys = [False, False, False, False]  # UP, LEFT, DOWN, RUGHT

Mario = pygame.image.load("MarioStanding.png")
bg = pygame.image.load("parkBackground.jpeg")
