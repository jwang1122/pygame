from appsuper import *

class Apple:
    def __init__(self):
        self.image, self.rect = loadImage("apple3.png")
        self.next()
    
    def draw(self):
        Game.screen.blit(self.image, self.rect)

    def next(self):
        self.rect.topleft = randomPoint()

class Snake:
    def __init__(self):
        self.head, self.rectHead = loadImage("head.png")
        self.body, self.rectBody = loadImage("body.jpg")
        self.speed = (0, 40)
        self.move()
    
    def draw(self):
        Game.screen.blit(self.head, self.rectHead)
        Game.screen.blit(self.body, self.rectBody)

    def move(self):
        self.rectHead.move_ip(self.speed)


class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        super().__init__(title, bg, fps)
        self.snake = Snake()
        self.apple = Apple()

    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()    