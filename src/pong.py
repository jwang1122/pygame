import pygame
from pygame.locals import *
from pygamelib import *
from appText import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (127,127,127)
YELLOW = (255,255,0)

class App:
    WIDTH = 640
    HEIGHT = 480
    SIZE = WIDTH, HEIGHT

    def __init__(self):
        pygame.init()
        App.screen = pygame.display.set_mode(self.SIZE)
        self.running = True

    def mainloop(self):
        while self.running:
            self.handleEvents()
            self.paint()
        pygame.quit()

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            self.handleEvent(event)

    def handleEvent(self, event):
        pass
    
    def paint(self):
        pass

   
class Ball:
    def __init__(self, pos, field, pad):
        self.pos = pos
        self.field = field
        self.pad = pad
        self.speed = [1, 1]
        self.color = YELLOW
        self.rect = pygame.Rect(pos, (20, 20))
    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.left < self.field.rect.left:
            self.speed[0] = abs(self.speed[0])
        if self.rect.right > self.field.rect.right:
            self.speed[0] = -abs(self.speed[0])
        if self.rect.top < self.field.rect.top:
            self.speed[1] = abs(self.speed[1])
        if self.rect.bottom > self.field.rect.bottom:
            self.speed[1] = -abs(self.speed[1])
        if self.rect.colliderect(self.pad.rect):
            self.speed[0] = abs(self.speed[0])
    
    def draw(self):
        pygame.draw.rect(App.screen, self.color, self.rect, 0)

class Pad:
    def __init__(self, keys, field):
        self.keys = keys
        self.field = field
        self.speed = [0, 0]
        self.v = 5
        self.color = GREEN
        self.rect = pygame.Rect(self.field.rect.topleft, (10, 50))
        self.rect.move_ip(10, 0)
    def do(self, event):
        if event.type == KEYDOWN:
            if event.key == self.keys[0]:
                self.speed[1] = -self.v
            if event.key == self.keys[1]:
                self.speed[1] = self.v
            elif event.type == KEYUP:
                self.speed[1] = 0

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.top < self.field.rect.top:
            self.rect.top = self.field.rect.top
        if self.rect.bottom > self.field.rect.bottom:
            self.rect.bottom = self.field.rect.bottom
    
    def draw(self):
        pygame.draw.rect(App.screen, self.color, self.rect, 0)

class Field:
    def __init__(self, rect):
        self.color = WHITE
        self.bg_color = BLACK
        self.stroke = 10
        self.rect = pygame.Rect(rect)
    def draw(self):
        pygame.draw.rect(App.screen, self.color, self.rect, self.stroke)
        pygame.draw.rect(App.screen, self.bg_color, self.rect, 0)

class PongDemo(App):
    """Play the game of Pong."""
    def __init__(self):
        super().__init__()
        self.field = Field((130, 150, 400, 200))
        self.pad = Pad((K_UP, K_DOWN), self.field)
        self.ball = Ball(self.field.rect.center, self.field, self.pad)
        self.bg_color = GRAY
        self.running = True

    def handleEvent(self, event):
        self.pad.do(event)

    def paint(self):       
        self.update()
        self.draw()

    def update(self):
        self.ball.update()
        self.pad.update()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.field.draw()
        self.ball.draw()
        self.pad.draw()
        Text(App.screen, 'Ping Pong Game', (170,80), fontsize=60, fontcolor=GREEN).draw()
        pygame.display.flip()

if __name__ == '__main__':
    PongDemo().mainloop()