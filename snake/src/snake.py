from appsuper import *

class Snake:
    SIZE = 40
    def __init__(self, apple):
        self.apple = apple
        self.bodies = []
        self.addBody(200, 120)
        self.addBody(200, 80)
        self.head, self.headRect = loadImage("head.png")
        self.tail, self.tailRect = loadImage("block.jpg")
        self.speed = (0, 40)
        self.crash = loadSound("crash.mp3")
        self.eating = loadSound("ding.mp3")

    def addBody(self, x, y):
        rect = Rect(x,y, Snake.SIZE, Snake.SIZE)
        self.bodies.append(rect)

    def move(self):
        for i in range(len(self.bodies)-1, 0, -1):
            self.bodies[i] = self.bodies[i-1]
        head = Rect(self.bodies[0]) # create a new Rect as head
        head.move_ip(self.speed) # move the head to new location
        self.bodies[0] = head # set the rect to the head location
        if head.colliderect(self.apple.rect): # hit apple
            self.eating.play()
            self.apple.next()
            self.addBody(-40,0)

        for i in range(3, len(self.bodies)-1): 
            if head.colliderect(self.bodies[i]): # hit its body
                self.crash.play()
                Game.gameover = True
                
        if not (0<=head.left<=Game.width and 0 <= head.top <= Game.height): # out of bound
            self.crash.play()
            Game.gameover = True

    def draw(self):
        self.move()
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
    gameover=False
    def __init__(self, fps=5):
        super().__init__(fps=fps)
        self.apple = Apple()
        self.snake = Snake(self.apple)
        self.bgMusic = loadSound("bg_music_1.mp3")
        self.eating = loadSound("ding.mp3")
        self.crash = loadSound("crash.mp3")
        self.bgMusic.play(-1, 0) # play(loops=0, start=0.0, fade_ms=0); -1 for infinite loop
        self.bg, rect = loadImage("background.jpg")

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN:
            if event.key in Game.speeds:
                self.snake.speed = Game.speeds[event.key]

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))
        if not self.gameover:
            self.snake.draw()
            self.apple.draw()
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