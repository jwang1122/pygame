import pygame
import os

pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game Window")

LEFT_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
LEFT_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(LEFT_SPACESHIP_IMAGE, (55, 40)), 90)

def drawWindow(x, y):
    win.fill((255,255,255))
    win.blit(LEFT_SPACESHIP, (x,y))
    pygame.display.update()

def gameLoop():
    clock = pygame.time.Clock()
    run = True
    x,y=0,0
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        x += 1
        y += 1
        drawWindow(x, y)
    pygame.quit()

if __name__ == '__main__':
    gameLoop()
