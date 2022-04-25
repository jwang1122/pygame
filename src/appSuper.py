from ctypes.wintypes import SIZE
import pygame
from pygame.locals import *
import os
from random import randint


def jump(t, v0=1, y0=0, scale=10000, g = -9.807):
    y=(y0 + v0*t + g*t**2/2)*scale
    return int(y)

def drawText(text, pos, forecolor=(0,0,0)):
    font = pygame.font.SysFont('Arial Bold', 25)    
    img = font.render(text, True, forecolor)
    AppSuper.screen.blit(img, pos)

def randomPoint(size=40):
    rows = AppSuper.width/size-1
    cols = AppSuper.height/size-1
    x = randint(0, rows)*size
    y = randint(0, cols)*size
    return (x, y)

def randomPoints(n):
    points = []
    for i in range(n):
        p = randomPoint()
        points.append(p)
    return points

def randomRects(n, width, height):
    rects = []
    for i in range(n):
        pos = randomPoint()
        rects.append(Rect(pos, (width, height)))
    return rects


# def randomRects(n):
#     rects = []
#     for i in range(n):
#         r = Rect(randomPoint(), (20, 20))
#         rects.append(r)
#     return rects

def loadImage(filename, scale=1):
    filename = os.path.join('src/resources',filename)
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
    rect = image.get_rect()
    return image, rect

def loadSound(filename):
    pygame.mixer.init()
    filename = os.path.join('src/resources', filename)
    return pygame.mixer.Sound(filename)

class AppSuper:
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    arrowKeys = {K_LEFT:(-15, 0), K_RIGHT:(15, 0), K_UP:(0, -15),K_DOWN:(0, 15)}
    speeds = {K_LEFT:(-40, 0), K_RIGHT:(40, 0), K_UP:(0, -40),K_DOWN:(0, 40)}
    directions = {K_LEFT:LEFT, K_RIGHT:RIGHT, K_UP:UP,K_DOWN:DOWN}

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
    CYAN = (0, 255,255)

    def __init__(self, title="PyGame", bg=CYAN, fps=30):
        pygame.init()
        pygame.mixer.init()
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
    # AppSuper().mainloop()
    v0 = 0.49
    t = 100
    height = jump(0.05, v0)
    print(height)