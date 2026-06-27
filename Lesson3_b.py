# On mouse click the circle color will change

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click on the circle")

WHITE = (255, 255, 255)

circle_x = 300
circle_y = 200
radius = 40
circle_color = (0, 128, 255)

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            distance = ((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2) ** 0.5

            if distance <= radius:
                circle_color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )

    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), radius)
    pygame.display.update()
pygame.quit()
