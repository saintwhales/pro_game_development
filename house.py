import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((3, 219, 252))

    pygame.draw.rect(screen, (207, 75, 19), (100, 75, 900, 400))
    pygame.display.update()

pygame.quit()
