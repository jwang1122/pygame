import pygame
from pygame.locals import *
from pygamelib import *
import os

BLACK=(0,0,0)
GRAY = (127, 127, 127)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
MAGENTA = (255,0,255)

def loadImage(filename, scale=1):
    filename = os.path.join('src/resources',filename)
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))
    rect = image.get_rect()
    return image, rect

class App:
    running = True
    flags = RESIZABLE
    WIDTH = 640
    HEIGHT = 480
    SIZE = WIDTH, HEIGHT
    screen = pygame.display.set_mode(SIZE, flags)
    scenes = []
    def __init__(self, title="Python Game", bg=CYAN, fps=30):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.display.set_caption(title)
        self.bg = bg
        self.fps = fps
        self.clock = pygame.time.Clock()

    def toggleFullscreen(self):
        self.flags ^= FULLSCREEN
        pygame.display.set_mode((0,0), self.flags)

    def toggleResizable(self):
        self.flags ^= RESIZABLE
        pygame.display.set_mode(Rect(0,0,self.WIDTH, self.HEIGHT))

    def toggleFrame(self):
        self.flags ^= NOFRAME
        pygame.display.set_mode(self.SIZE, self.flags)

    def paint(self):
        self.screen.fill(self.bg)
        Text(self.screen, "Hello world!", (100,100), fontcolor=BLUE).draw()
        text = Text(self.screen, "Welcome to PyGame!",(100, 180),"curlz", 30, (255,0,0))
        text.draw()
        text.setPos((50, 220)).draw()
        text.setPos((50, 250)).setFont(fontcolor=BLACK).draw()
        
        pygame.display.update()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            self.handle(event)
            
    def handle(self, event):
        pass

    def mainloop(self):
        """Run the main event loop."""
        while self.running:
            self.clock.tick(self.fps)
            self.eventHandler()
            self.paint()
        pygame.quit()

class Text:
    def __init__(self, screen, text, pos, fontname='Arial Bold', fontsize=72, fontcolor=(0,0,0)):
        self.text = text
        self.pos = pos
        self.screen = screen
        self.setFont(fontname, fontsize, fontcolor)
        self.render()

    def setFont(self, fontname='Arial Bold', fontsize=72, fontcolor=(0,0,0)):
        """Set the Font object from name and size."""
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = fontcolor
        self.font = pygame.font.SysFont(fontname, fontsize)
        self.render()
        return self

    def setPos(self, pos):
        self.pos = pos
        self.render()
        return self

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.screen.blit(self.img, self.rect)

if __name__ == '__main__':
    App().mainloop()
