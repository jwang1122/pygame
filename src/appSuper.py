import pygame
from pygame.locals import *
import os
from random import randint

def draw_text(text, pos):
    font = pygame.font.SysFont('Arial Bold', 25)    
    img = font.render(text, True, AppSuper.BLACK)
    AppSuper.screen.blit(img, pos)

def random_point():
    x = randint(0, AppSuper.width)
    y = randint(0, AppSuper.height)
    return (x, y)

def random_points(n):
    points = []
    for i in range(n):
        p = random_point()
        points.append(p)
    return points

def random_rects(n):
    rects = []
    for i in range(n):
        r = Rect(random_point(), (20, 20))
        rects.append(r)
    return rects

def loadImage(filename, scale=1):
    filename = os.path.join('src/resources',filename)
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
    rect = image.get_rect()
    return image, rect

def loadSound(filename):
    filename = os.path.join('src/resources', filename)
    return pygame.mixer.Sound(filename)

class AppSuper:
    arrowKeys = {K_LEFT:(-15, 0), K_RIGHT:(15, 0), K_UP:(0, -15),K_DOWN:(0, 15)}

    running = True
    flags = RESIZABLE
    width=640
    height=480
    screen = pygame.display.set_mode((width,height), flags)
    RED = (255, 0, 0)
    GRAY = (150, 150, 150)
    BLUE = (0,0,255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    BLACK = (0,0,0)

    def __init__(self, title="PyGame", bg=(0, 255, 255), fps=30):
        pygame.init()
        pygame.display.set_caption(title)
        self.bg = bg
        self.fps = fps
        self.clock = pygame.time.Clock()

    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        pygame.display.update()

    def mainloop(self):
        running = True
        while running: 
            self.clock.tick(self.fps) # FPS: frame per second
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                self.handleEvent(event)
            self.paint()
            
        pygame.quit()

if __name__ == '__main__':
    AppSuper().mainloop()