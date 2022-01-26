import pygame as pg
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "resources")
width = 1280
height=480
screen = pg.display.set_mode((width, height), pg.SCALED)
pg.init()
snd = pg.mixer.Sound('src/resources/yunque.mp3')
snd.play()     

# functions to create our resources
def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    image = image.convert()

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

class Chimp(pg.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
    monkey when it is punched."""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = load_image("chimp.png", -1, 0.8)
        # self.image = pg.transform.scale(self.image, (250,250))
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False

def mainloop():
    clock = pg.time.Clock()
    running = True
    chimp = Chimp()
    xspeed = 5
    yspeed = 5

    while(running):
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
        screen.fill((0,255,255))
        x = chimp.rect.center[0]+xspeed
        y = chimp.rect.center[1]+yspeed
        if x > width or x < 0:
            xspeed = -xspeed
        if y > height or y<0:
            yspeed = -yspeed
        chimp.rect.center = (x,y)
        screen.blit(chimp.image, chimp.rect)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    mainloop()