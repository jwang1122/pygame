import pygame
import os

pygame.init()
size = 630, 300

window = pygame.display.set_mode(size)
pygame.display.set_caption("Draw Rectangle")

BLACK=(0,0,0)
GRAY = (127, 127, 127)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
MAGENTA = (255,0,255)
bg = GRAY

runing = True
start, end = (0,0)
while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            start = event.pos
            size = 0,0
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]

            window.fill(bg)
            pygame.draw.rect(window, RED, (start, size), 2)
            pygame.display.update()

pygame.quit()
