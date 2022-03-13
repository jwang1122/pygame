from appsuper import *
from appsuper import loadSound

class Snake:
    SIZE = 40
    def __init__(self):
        self.x = [40, 40]
        self.y = [40, 0]
        self.head, self.headRect = loadImage("head.png")
        self.tail, self.tailRect = loadImage("block.jpg")
        self.speed = (0, 40)

    def walk(self):
        for i in range(len(self.x)-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        self.x[0] += self.speed[0]
        self.y[0] += self.speed[1]

        self.draw()

    def draw(self):
        for i in range(len(self.x)):
            if i==0:
                Game.screen.blit(self.head, (self.x[i], self.y[i]))
            else:
                Game.screen.blit(self.tail, (self.x[i], self.y[i]))

class Apple:
    def __init__(self):
        self.image = pygame.image.load("snake/resources/apple.jpg")
        self.rect = self.image.get_rect()
        self.rect.topleft = random_point()

    def next(self):
        self.rect.topleft = random_point()

    def draw(self):
        Game.screen.blit(self.image, self.rect)

class Game(AppSuper):
    def __init__(self):
        super().__init__()
        self.apple = Apple()
        self.snake = Snake()
        self.bgMusic = loadSound("bg_music_1.mp3")
        self.eating = loadSound("ding.mp3")
        self.bgMusic.play(-1, 0) # play(loops=0, start=0.0, fade_ms=0); -1 for infinite loop
        self.bg, rect = loadImage("background.jpg")

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN:
            if event.key in Game.arrowKeys:
                self.snake.speed = Game.arrowKeys[event.key]

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))
        self.snake.walk()
        self.apple.draw()
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.rect.left, self.apple.rect.top):
            self.eating.play()
            self.apple.next()
            self.snake.x.append(-1)
            self.snake.y.append(-1)

        self.displayScore()
        pygame.display.update()

    def displayScore(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {len(self.snake.x)}",True,(200,200,200))
        Game.screen.blit(score,(850,10))

    def collision(self, x1, y1, x2, y2):
        rect1 = Rect(x1, y1, 40, 40)
        rect2 = Rect(x2, y2, 40, 40)
        return rect1.colliderect(rect2)

if __name__ == '__main__':
    Game().mainloop()