from appsuper import *

class Fighter():
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
        self.speed = 5
        self.index = 0
    
    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.fighter.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()