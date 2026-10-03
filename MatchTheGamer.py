import pygame

pygame.init()

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Match The Following Gamers")

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 150, 0)
red = (200, 0, 0)
blue = (0, 100, 200)

screen.fill(blue)

archer = pygame.image.load("archer.png")
ninja = pygame.image.load("ninja.png")
wizard = pygame.image.load("wizard.png")


font = pygame.font.SysFont("ariel", 28)

images = [
    (archer, (100, 50), "Bow"),
    (ninja, (100, 250), "Sword"),
    (wizard, (100, 420), "Wand"),
]

right_names = [
    ("Sword", (600, 80)),
    ("Wand", (600, 300)),
    ("Bow", (600, 500)),
]

for img, pos, name in images:
    screen.blit(img, pos)

for (
    text,
    pos,
) in right_names:
    t = font.render(text, True, black)
    screen.blit(t, pos)

pygame.display.update()

selected_left = None
selected_pos = None
match_count = 0
wrong_match = False
total_attempts = 0

running = True

while running:
    event = pygame.event.poll()

    # Close window
    if event.type == pygame.QUIT:
        running = False

    # Mouse clicked
    if event.type == pygame.MOUSEBUTTONDOWN:

        x, y = pygame.mouse.get_pos()

        for img, pos, name in images:

            rect = img.get_rect(topleft=pos)

            if rect.collidepoint(x, y):

                selected_left = name

                selected_pos = (pos[0] + 120, pos[1] + 40)

        for text, pos in right_names:
            text_surface = font.render(text, True, black)
            text_rect = text_surface.get_rect(topleft=pos)
            if text_rect.collidepoint(x, y) and selected_left:
                pygame.draw.line(screen, black, selected_pos, (pos[0], pos[1] + 15), 3)
                pygame.display.update()
                total_attempts += 1
                if selected_left == text:
                    match_count += 1
                else:
                    wrong_match = True
                selected_left = None
            if total_attempts == 3:

                screen.fill(white)
                if wrong_match:
                    result = font.render("LOSER", True, red)
                else:
                    result = font.render("WINNER", True, green)
                screen.blit(result, (350, 250))

                pygame.display.update()
                result_screen = True

                while result_screen:

                    result_event = pygame.event.wait()

                    if result_event.type == pygame.QUIT:
                        result_screen = False
                        runnong = False
pygame.quit()
