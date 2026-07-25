import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((3, 219, 252))

    pygame.draw.rect(screen, (46, 230, 30), (0, 450, 1000, 250))
    pygame.draw.rect(screen, (207, 75, 19), (300, 200, 400, 350))
    pygame.draw.polygon(screen, (0, 0, 0), [(275, 200), (725, 200), (500, 50)])
    pygame.draw.rect(screen, (156, 91, 22), (450, 400, 100, 150))
    pygame.display.update()

pygame.quit()
