import pygame
import os

from main import main

pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game Window")

LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (55, 40)), 90)

def drawWindow():
    win.fill((255,255,255))
    win.blit(LEFT_SPACESHIP, (100,100))
    pygame.display.update()

def gameLoop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        drawWindow()
    pygame.quit()

if __name__ == '__main__':
    gameLoop()
