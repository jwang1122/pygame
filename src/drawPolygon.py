import pygame
import os

pygame.init()
size = 640, 480

window = pygame.display.set_mode(size, pygame.RESIZABLE)
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
bg = CYAN

runing = True
while runing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runing = False
    window.fill(bg)
    pygame.draw.polygon(window, RED, [(50, 20), (60, 100), (400,300), (10,320)], 4)
    pygame.draw.polygon(window, BLUE, [(150, 20), (360, 100), (40,300), (310,320)], 0)
    pygame.display.update()

pygame.quit()
