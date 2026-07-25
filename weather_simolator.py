import pygame
import random

# ----------Initaialize----------
pygame.init()

WIDTH = 900
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weather Simulator")

clock = pygame.time.Clock()

# ----------Colors----------
SKY = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 120, 255)
GREEN = (60, 180, 75)

font = pygame.font.SysFont(None, 30)

weather = "Sunny"

# ----------Clouds----------
clouds = []

for i in range(5):
    x = random.randint(0, WIDTH)
    y = random.randint(30, 280)
    clouds.append([x, y])

# ----------Rain----------
raindrops = []

for i in range(250):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, HEIGHT)
    raindrops.append([x, y])

# ----------Snow----------
snowflakes = []

for i in range(200):
    x = random.randint(0, WIDTH)
    y = random.randint(-HEIGHT, HEIGHT)
    size = random.randint(2, 5)
    snowflakes.append([x, y, size])

# ----------Buttons----------
sun_button = pygame.Rect(60, 525, 120, 50)
rain_button = pygame.Rect(250, 525, 120, 50)
snow_button = pygame.Rect(440, 525, 120, 50)

# ===========================
running = True

while running:

    # ----------Background----------
    screen.fill(SKY)

    # ----------Sun----------
    if weather == "Sunny":

        pygame.draw.circle(screen, YELLOW, (760, 100), 55)

        # Sun Rays
        for angle in range(0, 360, 30):

            x1 = 760 + 65 * pygame.math.Vector2(1, 0).rotate(angle).x
            y1 = 100 + 65 * pygame.math.Vector2(1, 0).rotate(angle).y

            x2 = 720 + 85 * pygame.math.Vector2(1, 0).rotate(angle).x
            y2 = 100 + 85 * pygame.math.Vector2(1, 0).rotate(angle).y

            pygame.draw.line(screen, YELLOW, (x1, y1), (x2, y2), 3)

    # ----------Clouds----------
    if weather == "Rain":
        cloud_color = (70, 70, 70)
    else:
        cloud_color = WHITE

    for cloud in clouds:

        pygame.draw.circle(screen, cloud_color, (cloud[0], cloud[1]), 25)
        pygame.draw.circle(screen, cloud_color, (cloud[0] + 25, cloud[1] - 10), 30)
        pygame.draw.circle(screen, cloud_color, (cloud[0] + 55, cloud[1]), 25)

        cloud[0] += 1

        if cloud[0] > WIDTH + 60:
            cloud[0] = -60
