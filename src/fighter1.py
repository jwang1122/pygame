from appsuper import *

class Player:
    def __init__(self) -> None:
        self.img, self.rect = loadImage("fighterjet1.png")
        self.rect.center = (600, 250)
    def draw(self):
        Game.screen.blit(self.img, self.rect)
    
    def move(self, speed):
        self.rect.move_ip(speed)

class Fighter:
    def __init__(self) -> None:
        self.img, self.rect = loadImage("fighter4.png")
        self.speed = 5
        self.fighters = []
        for i in range(10):
            rect = pygame.Rect(random_point(), self.rect.size)
            self.fighters.append(rect)

    def draw(self):
        for rect in self.fighters:
            rect.left += self.speed
            if rect.left>Game.width:
                rect.right = 0
            Game.screen.blit(self.img, rect)

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        super().__init__(title, bg, fps)
        self.fighter = Fighter()
        self.player = Player()
        self.speed = 5
    
    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN and event.key in self.arrowKeys:
            self.player.move(self.arrowKeys[event.key])

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.fighter.draw()
        self.player.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()