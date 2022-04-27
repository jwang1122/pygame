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
        self.rectHead.move_ip(0, 40)
        self.bodies = [] # bodies holds rects for snake where index=0 is the head
        self.bodies.append(self.rectHead)
        self.bodies.append(self.rectBody)
    
    def draw(self):
        Game.screen.blit(self.head, self.bodies[0])
        for i in range(1,len(self.bodies)):
            Game.screen.blit(self.body, self.bodies[i])

    def move(self):
        pass


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