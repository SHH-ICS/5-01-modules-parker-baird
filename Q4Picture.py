import pygame
import sys

def Q4Picture():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Q4Picture")

    blue = (0, 0, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, blue, (50, 50, 100, 100)) 
    pygame.draw.circle(screen, green, (200, 200), 50)
    pygame.draw.line(screen, red, (300, 300), (400, 300), 5)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()