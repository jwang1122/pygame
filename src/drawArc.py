import pygame
import math

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

rect = pygame.Rect(100,100,100,100)

runing = True
while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing = False
    window.fill(bg)
    pygame.draw.arc(window, RED, rect, 0, math.pi/2, 2)
    pygame.draw.rect(window, GREEN, rect, 2)
    pygame.draw.arc(window, GREEN,[210, 75, 150, 125], math.pi/2, math.pi, 2)
    pygame.draw.rect(window, BLACK, [210, 75, 150, 125], 2)
    pygame.display.update()

pygame.quit()
