import pygame
import random

# Initialise

pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars Driving on Road")

clock = pygame.time.Clock()

# Colours

SKY = (135, 206, 235)
BLACK = (0, 0, 0)
BLUE = (3, 61, 252)
GREEN = (60, 180, 75)
YELLOW = (255, 255, 0)

carx = random.randint(0, WIDTH)
car = pygame.image.load("car.png")


running = True

while running:

    # Background
    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 350, WIDTH, 550))

    # Road
    pygame.draw.rect(screen, BLACK, (0, 350, WIDTH, 80))

    # Sun
    pygame.draw.circle(screen, YELLOW, (450, 100), 55)

    # Sun Rays
    for angle in range(0, 360, 30):

        x1 = 450 + 65 * pygame.math.Vector2(1, 0).rotate(angle).x
        y1 = 100 + 65 * pygame.math.Vector2(1, 0).rotate(angle).y

        x2 = 450 + 85 * pygame.math.Vector2(1, 0).rotate(angle).x
        y2 = 100 + 85 * pygame.math.Vector2(1, 0).rotate(angle).y

        pygame.draw.line(screen, YELLOW, (x1, y1), (x2, y2), 3)

    # Cars
    screen.blit(car, (carx, 50))
    carx += 10

    if carx > WIDTH + 60:
        carx = -500

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
