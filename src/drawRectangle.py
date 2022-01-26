import pygame
import os

pygame.init()
size = 600, 300

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
    window.fill(bg)
    pygame.draw.rect(window, RED, (50, 20, 120, 100))
    pygame.draw.rect(window, GREEN, (100, 60, 120, 100))
    pygame.draw.rect(window, BLUE, (150, 100, 120, 100))
    pygame.draw.rect(window, RED, (350, 20, 120, 100), 1)
    pygame.draw.rect(window, GREEN, (400, 60, 120, 100), 4)
    pygame.draw.rect(window, BLUE, (450, 100, 120, 100), 8)    
    pygame.display.update()

pygame.quit()
