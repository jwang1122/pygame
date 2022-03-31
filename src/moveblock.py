from appsuper import *

class Landscape:
    def __init__(self) -> None:
        self.walls = [[30,50,100,80],[130, 100, 130, 30],[260,100, 30, 200]]

    def draw(self):
        for r in self.walls:
            rect = pygame.Rect(r[0], r[1], r[2], r[3])
            pygame.draw.rect(Game.screen, Game.BLACK, rect )

class Player:
    def __init__(self, landscape) -> None:
        self.rect = pygame.Rect(10, 150, 40, 40)
        self.landscape = landscape

    def draw(self):
        pygame.draw.rect(Game.screen, Game.RED, self.rect, 2)

    def move(self, speed):
        rect = self.rect.copy()
        rect.move_ip(speed)
        if not self.collide(rect):
            self.rect.move_ip(speed)

    def collide(self, rect):
        for r in self.landscape.walls:
            r1 = pygame.Rect(r[0], r[1], r[2], r[3])
            if rect.colliderect(r1):
                return True
        return False

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(255,255,0), fps=30):
        super().__init__(title, bg, fps)
        self.walls = Landscape()
        self.player = Player(self.walls)

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN and event.key in self.arrowKeys:
            self.player.move(self.arrowKeys[event.key])


    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.walls.draw()
        self.player.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()