import pygame

from main import main

size = 900, 500
win = pygame.display.set_mode(size)
pygame.display.set_caption("Game Window")

run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
pygame.quit()


