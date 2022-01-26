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
punchSound = pg.mixer.Sound('src/resources/punch.wav')    
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

def mainloop():
    clock = pg.time.Clock()
    running = True
    fist = Fist()
    punching = False

    while(running):
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running=False
            elif event.type == pg.MOUSEBUTTONDOWN:
                punchSound.play()
                punching = True
            elif event.type == pg.MOUSEBUTTONUP:
                punching = False

        screen.fill((0,255,255))
        fist.update()
        if punching:
            fist.rect.move_ip(10,-17)
        screen.blit(fist.image, fist.rect)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    mainloop()