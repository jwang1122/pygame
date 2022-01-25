import pygame
from pygame.locals import *

pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
'midtop', 'midright', 'midbottom', 'midleft', 'center')

SIZE = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)
GREEN = (0,255,0)
pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = pygame.Rect(20, 20, 300, 120)

topleft = rect.topleft
print(topleft)
print(eval('rect.center'))
x=5
print(eval('x'))

def draw_text(pt, pos):
    font = pygame.font.SysFont('Arial Bold', 25)
    screen.blit(font.render(pt, True, (0,0,255)), pos)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 4)
    for pt in pts:
        pos = eval('rect.' + pt)
        draw_text(pt, pos)
        pygame.draw.circle(screen, RED, pos, 3)
    pygame.display.flip()
pygame.quit()
