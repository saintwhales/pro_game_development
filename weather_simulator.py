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

            x2 = 760 + 85 * pygame.math.Vector2(1, 0).rotate(angle).x
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

    # ----------- Rain ----------
    if weather == "Rain":
        for drop in raindrops:

            pygame.draw.line(
                screen, BLUE, (drop[0], drop[1]), (drop[0], drop[1] + 12), 2
            )

            drop[1] += 10

            if drop[1] > HEIGHT:
                drop[1] = random.randint(-100, 0)
                drop[0] = random.randint(0, WIDTH)

    # ---------- Snow ----------
    if weather == "Snow":

        for snow in snowflakes:

            pygame.draw.circle(screen, WHITE, (snow[0], snow[1]), snow[2])

            snow[1] += 2
            snow[0] += random.randint(-1, 1)

            if snow[1] > HEIGHT:
                snow[1] = random.randint(-100, 0)
                snow[0] = random.randint(0, WIDTH)

    # ---------- Ground ----------
    if weather == "Snow":
        ground_color = WHITE
    else:
        ground_color = GREEN

    pygame.draw.rect(screen, ground_color, (0, 420, WIDTH, 180))

    # ---------- Snowman ----------
    if weather == "Snow":

        # Bottom Body
        pygame.draw.circle(screen, WHITE, (730, 355), 55)

        # Middle Body
        pygame.draw.circle(screen, WHITE, (730, 275), 42)

        # Head
        pygame.draw.circle(screen, WHITE, (730, 215), 28)

        # Eyes
        pygame.draw.circle(screen, BLACK, (722, 208), 3)
        pygame.draw.circle(screen, BLACK, (738, 208), 3)

        # Smile
        pygame.draw.arc(screen, BLACK, (716, 217, 28, 18), 3.5, 5.9, 1)

        # Carrot Nose
        pygame.draw.polygon(screen, (255, 140, 0), [(730, 218), (748, 221), (730, 224)])

        # Buttons
        pygame.draw.circle(screen, BLACK, (730, 260), 4)
        pygame.draw.circle(screen, BLACK, (730, 275), 4)
        pygame.draw.circle(screen, BLACK, (730, 290), 4)

        # Arms
        pygame.draw.line(screen, (120, 70, 20), (690, 275), (645, 235), 3)
        pygame.draw.line(screen, (120, 70, 20), (770, 275), (815, 235), 3)

        # Hat Brim
        pygame.draw.rect(screen, BLACK, (705, 180, 50, 8))

        # Hat Top
        pygame.draw.rect(screen, BLACK, (715, 135, 30, 45))

    # ---------- Buttons ----------
    pygame.draw.rect(screen, (255, 210, 0), sun_button, border_radius=10)
    pygame.draw.rect(screen, (90, 140, 255), rain_button, border_radius=10)
    pygame.draw.rect(screen, (220, 220, 220), snow_button, border_radius=10)

    screen.blit(font.render("Sunny", True, BLACK), (82, 540))
    screen.blit(font.render("Rain", True, BLACK), (280, 540))
    screen.blit(font.render("snow", True, BLACK), (468, 540))

    # Current Weather
    text = font.render("Current Weather: " + weather, True, BLACK)
    screen.blit(text, (610, 535))

    # ---------- Events -----------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            if sun_button.collidepoint(event.pos):
                weather = "Sunny"

            elif rain_button.collidepoint(event.pos):
                weather = "Rain"

            elif snow_button.collidepoint(event.pos):
                weather = "Snow"

    pygame.display.update()
    clock.tick(60)

pygame.quit()
