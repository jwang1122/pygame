import pygame as pg
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")
width = 1280
height=480
screen = pg.display.set_mode((width, height), pg.SCALED)
pg.init()
snd = pg.mixer.Sound('src/data/yunque.mp3')
snd.play() 
punchSound = pg.mixer.Sound('src/data/punch.wav')    
# pg.mouse.set_visible(False)

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

# classes for our game objects
class Fist(pg.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("fist.png", -1, 1)
        self.image = pg.transform.scale(self.image, (150,150))
        self.fist_offset = (0, 0)
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(-80, -80)

    def punch(self, chimp):
        print(self.rect)
        print(chimp.rect)
        return self.rect.colliderect(chimp.rect)

def mainloop():
    clock = pg.time.Clock()
    running = True
    chimp = Chimp()
    xspeed = 15
    yspeed = 15
    fist = Fist()

    while(running):
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punchSound.play()
                else:
                    print("missed!")
        screen.fill((0,255,255))
        x = chimp.rect.center[0]+xspeed
        y = chimp.rect.center[1]+yspeed
        if x > width:
            xspeed = -5
        if y > height:
            yspeed = -5
        if x <0:
            xspeed = 5
        if y<0:
            yspeed= 5
        chimp.rect.center = (x,y)
        screen.blit(chimp.image, chimp.rect)
        screen.blit(fist.image, fist.rect)
        fist.update()
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    mainloop()