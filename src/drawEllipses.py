import pygame
import os

pygame.init()
size = 630, 300

window = pygame.display.set_mode(size)
pygame.display.set_caption("Draw Rectangle")

bg = (127,127,127)
BLACK=(0,0,0)
GRAY = (127, 127, 127)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
MAGENTA = (255,0,255)

runing = True
while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event)
            print(event.pos)
            print(event.button)
    window.fill(bg)
    pygame.draw.ellipse(window, RED, (50, 20, 160, 100))
    pygame.draw.ellipse(window, GREEN, (100, 60, 160, 100))
    pygame.draw.ellipse(window, BLUE, (150, 100, 160, 100))
    pygame.draw.ellipse(window, RED, (350, 20, 160, 100), 1)
    pygame.draw.ellipse(window, GREEN, (400, 60, 160, 100), 4)
    pygame.draw.ellipse(window, BLUE, (450, 100, 160, 100), 8)   
    pygame.display.update()

pygame.quit()
