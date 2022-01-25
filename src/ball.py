import pygame
from pygame.locals import *
import os

size = 640, 320
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)
WHITE = (255,255,255)
pygame.init()
screen = pygame.display.set_mode(size)
running = True

ball = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'diamondJ.gif')), (80,100))
rect = ball.get_rect()
speed = [2, 2]

clock = pygame.time.Clock()
bound = 20
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    rect = rect.move(speed)
    if rect.left < 0 or rect.right > width:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(GREEN)
    pygame.draw.rect(screen, RED, rect, 1)
    screen.blit(ball, rect)
    pygame.display.update()

pygame.quit()
