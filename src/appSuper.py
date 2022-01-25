import pygame
from pygame.locals import *

class AppSuper:
    running = True
    flags = RESIZABLE
    screen = pygame.display.set_mode((640, 480), flags)
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        pygame.display.set_caption("Game Window")
        self.bg = (0, 255, 255)
        self.clock = pygame.time.Clock()
        # self.mainloop()
    
    def paint(self):
        self.screen.fill(self.bg)
        pygame.display.update()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                AppSuper.running = False
            
 
    def mainloop(self):
        """Run the main event loop."""
        while self.running:
            self.clock.tick(1)
            self.eventHandler()
            self.paint()
        pygame.quit()

if __name__ == '__main__':
    AppSuper()