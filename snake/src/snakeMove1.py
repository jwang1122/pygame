from appsuper import *
from appsuper import loadSound

class Snake:
    SIZE = 40
    def __init__(self):
        self.bodies = []
        self.head, rect = loadImage("head.png")
        self.tail, rect = loadImage("block.jpg")
        self.addBody(200, 120)
        self.addBody(200, 160)
        self.speed = (0, 40)

    def addBody(self, left, top):
        rect = Rect(left, top, Snake.SIZE, Snake.SIZE)
        self.bodies.append(rect)

    def walk(self):
        for i in range(len(self.bodies)-1, 0, -1):
            self.bodies[i] = self.bodies[i-1]
        rect = Rect(self.bodies[0].left, self.bodies[0].top, Snake.SIZE, Snake.SIZE)  
        rect.move_ip(self.speed)      
        self.bodies[0] = rect 

    def draw(self):
        self.walk()
        for i in range(len(self.bodies)):
            if i==0:
                Game.screen.blit(self.head, self.bodies[0])
            else:
                Game.screen.blit(self.tail, self.bodies[i])

class Apple:
    def __init__(self):
        self.image = pygame.image.load("snake/resources/apple.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = randomPoint()

    def draw(self):
        Game.screen.blit(self.image, self.rect)

class Game(AppSuper):
    def __init__(self, fps=2):
        super().__init__(fps=fps)
        self.apple = Apple()
        self.snake = Snake()
        self.bgMusic = loadSound("bg_music_1.mp3")
        self.bgMusic.play(-1, 0) # play(loops=0, start=0.0, fade_ms=0); -1 for infinite loop
        self.bg, rect = loadImage("background.jpg")

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN:
            if event.key in Game.arrowKeys:
                self.snake.speed = Game.arrowKeys[event.key]

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()