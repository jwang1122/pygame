import pygame
from pygame.locals import *

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
'midtop', 'midright', 'midbottom', 'midleft', 'center')

HEIGHT = 480
WIDTH = 640
SIZE = WIDTH, HEIGHT
RED = (255, 0, 0)
CYAN = (0, 255, 255)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("PyGame Coordinates")

rect = pygame.Rect(0, 0, WIDTH, HEIGHT)

def draw_text(pt, pos):
    font = pygame.font.SysFont('Arial Bold', 25)
    screen.blit(font.render(pt, True, BLUE), pos)

def paint():
    screen.fill(CYAN)
    pygame.draw.line(screen, RED, rect.midtop, rect.midbottom, 1)
    pygame.draw.line(screen, RED, rect.midleft, rect.midright, 1)
    pygame.draw.line(screen, RED, rect.topleft, rect.topright, 4)
    pygame.draw.line(screen, RED, rect.topleft, rect.bottomleft, 4)
    pygame.draw.polygon(screen, RED,[(625, -10),(640,0),(625, 10)], 0)
    pygame.draw.polygon(screen, RED,[(0, 465),(0,480),(10, 465)], 0)
    pygame.draw.circle(screen, BLUE, (0,0), 10)
    pygame.draw.circle(screen, BLUE, rect.center, 5)
    draw_text('(0, 0)', (5,5))
    draw_text('(640, 0)', (580,15))
    draw_text('(0, 480)', (15,460))
    draw_text('(320, 240)', (325,250))
    pygame.display.flip()

running = True
clock = pygame.time.Clock()
while running:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    paint()

pygame.quit()
