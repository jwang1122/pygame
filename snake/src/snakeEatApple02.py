from appsuper import *

class Apple:
    def __init__(self):
        self.image, self.rect = loadImage("apple3.png")
        self.rect.topleft = (600, 440)
    
    def draw(self):
        Game.screen.blit(self.image, self.rect)

    def next(self):
        self.rect.topleft = randomPoint()

class Snake:
    def __init__(self):
        self.head, self.rectHead = loadImage("head.png")
        self.body, self.rectBody = loadImage("body.jpg")
        self.speed = (0, 40)
        self.rectHead.left = 600
        self.rectBody.topleft = (0, 440)
    
    def draw(self):
        Game.screen.blit(self.head, self.rectHead)
        Game.screen.blit(self.body, self.rectBody)

    def move(self):
        self.rectHead.move_ip(self.speed)


class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        super().__init__(title, bg, fps)
        self.bg, self.rect = loadImage("grassfield1.jpg")
        self.snake = Snake()
        self.apple = Apple()

    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, self.rect)
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()    