import pygame
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)


class Pane(object):
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Box Test')
        self.screen = pygame.display.set_mode((600,400), 0, 32)
        self.screen.fill((white))
        pygame.display.update()
        self.mainloop()


    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
        pygame.display.update()

    def addText(self):
        self.font = pygame.font.SysFont('Arial Bold', 50)
        self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
        pygame.display.update()
        
    def paint(self):
        self.addRect()
        self.addText()

    def mainloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.paint()
        pygame.quit()

if __name__ == '__main__':
    Pane()
