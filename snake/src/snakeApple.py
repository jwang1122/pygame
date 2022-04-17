from appsuper import *
from appsuper import loadSound

class Snake:
    def __init__(self):
        self.v = []
        self.head, self.headRect = loadImage("head.png")
        self.v.append((Game.width//2-20, Game.height//2-20))
        self.headRect.topleft = self.v[0]
        self.tail, self.tailRect = loadImage("block.jpg")
        self.v.append((self.v[0][0], self.v[0][1]-40))
        self.tailRect = self.v[1]

    def draw(self):
        for i in range(len(self.v)):
            if i==0:
                Game.screen.blit(self.head, self.headRect)
            else:
                Game.screen.blit(self.tail, self.v[i])

class Apple:
    def __init__(self):
        self.image = pygame.image.load("snake/resources/apple3.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = randomPoint()

    def draw(self):
        Game.screen.blit(self.image, self.rect)

class Game(AppSuper):
    def __init__(self):
        super().__init__()
        self.apple = Apple()
        self.snake = Snake()
        self.bgMusic = loadSound("bg_music_1.mp3")
        self.bgMusic.play(-1, 0) # play(loops=0, start=0.0, fade_ms=0); -1 for infinite loop
        self.bg, rect = loadImage("background.jpg")

    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))
        self.snake.draw()
        self.apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()