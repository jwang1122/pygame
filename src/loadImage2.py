import pygame as pg
import os

pg.init()
win = pg.display.set_mode((640, 480))
filename = os.path.join('src/resources','asteroid.png')
print(filename)
asteroid = pg.image.load(filename)

def paint():
    win.fill((0,0,0))
    win.blit(asteroid, (10,10))
    pg.display.update()  

def gameLoop():
    run = True
    while run:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                run = False
        paint()
    pg.quit()

if __name__ == '__main__':
    gameLoop()
