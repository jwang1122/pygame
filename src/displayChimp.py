import os
import pygame as pg

class Chimp:
    def __init__(self):
        self.image= pg.image.load("src/resources/chimp.png")
        self.image = pg.transform.scale(self.image, (250, 300))
        self.rect = self.image.get_rect()
class Fist:
    def __init__(self):
        self.image= pg.image.load("src/resources/fist.png")
        self.image = pg.transform.scale(self.image, (150,150))
        self.rect = self.image.get_rect()

def mainloop():
    clock = pg.time.Clock()
    running = True
    chimp = Chimp()
    fist = Fist()
    screen = pg.display.set_mode((1280, 480), pg.SCALED)
    while(running):
        clock.tick(1)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        chimp.rect.center = (700,200)
        screen.blit(chimp.image, chimp.rect)
        fist.rect.center = (100,100)
        fist.rect = fist.rect.move(200,200)
        screen.blit(fist.image, fist.rect)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    mainloop()