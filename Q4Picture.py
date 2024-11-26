import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Q4Picture")

blue = (34, 0, 50)
green = (23, 255, 10)
red = (255, 250, 0)

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