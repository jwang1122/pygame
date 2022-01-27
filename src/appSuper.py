import pygame
from pygame.locals import *
import sys

class AppSuper:
    running = True
    flags = RESIZABLE
    screen = pygame.display.set_mode((640, 480), flags)

    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.display.set_caption(title)
        self.bg = bg
        self.clock = pygame.time.Clock()
        self.fps = fps
    
    def paint(self):
        self.screen.fill(self.bg)
        pygame.display.update()

    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            self.eventHandler(event)
                
    def eventHandler(self, event):
        pass

    def mainloop(self):
        """Run the main event loop."""
        while self.running:
            self.clock.tick(self.fps)
            self.eventsHandler()
            self.paint()

if __name__ == '__main__':
    AppSuper("My Test", bg=(255,255,0)).mainloop()