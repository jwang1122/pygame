from appsuper import *

class Snake:
    SIZE = 40
    def __init__(self):
        self.bodies = []
        self.addBody(200, 120)
        self.addBody(200, 80)
        self.head, self.headRect = loadImage("head.png")
        self.tail, self.tailRect = loadImage("block.jpg")
        self.speed = (0, 40)

    def addBody(self, x, y):
        rect = Rect(x,y, Snake.SIZE, Snake.SIZE)
        self.bodies.append(rect)

    def walk(self):
        for i in range(len(self.bodies)-1, 0, -1):
            self.bodies[i] = self.bodies[i-1]
        rect = Rect(self.bodies[0]) # create a new Rect as head
        rect.move_ip(self.speed) # move the head to new location
        self.bodies[0] = rect # set the rect to the head location

    def draw(self):
        self.walk()
        for i in range(len(self.bodies)):
            if i==0:
                Game.screen.blit(self.head, self.bodies[0])
            else:
                pygame.draw.circle(Game.screen, (0,255,100), (self.bodies[i].left+20, self.bodies[i].top+20), 20, 0)

class Apple:
    def __init__(self):
        self.image, self.rect = loadImage("apple3.png")
        self.rect.topleft = randomPoint()

    def next(self):
        self.rect.topleft = randomPoint()

    def draw(self):
        Game.screen.blit(self.image, self.rect)

class Game(AppSuper):
    def __init__(self, fps=5):
        super().__init__(fps=fps)
        self.apple = Apple()
        self.snake = Snake()
        self.bgMusic = loadSound("bg_music_1.mp3")
        self.eating = loadSound("ding.mp3")
        self.crash = loadSound("crash.mp3")
        self.bgMusic.play(-1, 0) # play(loops=0, start=0.0, fade_ms=0); -1 for infinite loop
        self.bg, rect = loadImage("background.jpg")
        self.gameover=False

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN:
            if event.key in Game.arrowKeys:
                self.snake.speed = Game.arrowKeys[event.key]

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))
        if not self.gameover:
            self.snake.draw()
            self.apple.draw()
            if self.snake.bodies[0].colliderect(self.apple.rect):
                self.eating.play()
                self.apple.next()
                self.snake.addBody(-1,-1)

            for i in range(3, len(self.snake.bodies)-1):
                if self.snake.bodies[0].colliderect(self.snake.bodies[i]):
                    self.crash.play()
                    self.gameover = True
                    
            if not (0<=self.snake.bodies[0].left<=Game.width and 0 <= self.snake.bodies[0].top <= Game.height):
                self.crash.play()
                self.snake.speed = (0,0)
                self.gameover = True
        else:
            img,rect = loadImage("gameover1.png")
            rect.move_ip((250,150))
            Game.screen.blit(img, rect)

        self.displayScore()
        pygame.display.update()

    def displayScore(self):
        drawText(f"Score: {len(self.snake.bodies)}", (700, 10), (255,255,255))

if __name__ == '__main__':
    Game().mainloop()