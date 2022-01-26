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
    pygame.draw.circle(window, RED, (150, 200), 100, 4)
    pygame.draw.circle(window, YELLOW, (350, 200), 50, 0)
    pygame.draw.circle(window, BLUE, [350, 350], 50, 0, draw_top_right=True)
    pygame.draw.circle(window, RED, [350, 350], 50, 30, draw_top_left=True)
    pygame.draw.circle(window, YELLOW, [350, 350], 50, 20, draw_bottom_left=True)
    pygame.draw.circle(window, BLACK, [350, 350], 50, 10, draw_bottom_right=True)
    pygame.display.update()

pygame.quit()
