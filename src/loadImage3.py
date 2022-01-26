from ctypes.wintypes import RECT
import pygame as pg
import os

pg.init()
width =640
height = 480
win = pg.display.set_mode((width, height))

def loadImage(filename, scale=1):
    filename = os.path.join('src/resources',filename)
    print(filename)
    image = pg.image.load(filename)
    image = pg.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
    rect = image.get_rect()
    return image, rect

def paint(image, rect):
    win.fill((0,0,0))
    win.blit(image, rect)
    pg.draw.rect(win, (0,255,0), rect, 4)
    pg.draw.line(win,(255,0,0),rect.midleft, rect.midright, 1)
    pg.draw.line(win,(255,0,0),rect.midtop, rect.midbottom, 1)
    pg.display.update()  

def gameLoop():
    clock = pg.time.Clock()
    image, rect = loadImage("asteroid.png", 0.5)
    x = 0
    y = 0
    xspeed = 2
    yspeed = 2
    run = True
    while run:
        clock.tick(30)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run = False
        x = rect.center[0] + xspeed
        y = rect.center[1] + yspeed
        if x > width or x<0:
            xspeed = -xspeed        
        if y > height or y < 0:
            yspeed = -yspeed
        rect.center = (x,y) # make the rect move with image
        paint(image, rect)
    pg.quit()

if __name__ == '__main__':
    gameLoop()
