from appsuper import *

class Cloud():
    def __init__(self) -> None:
        self.img, self.rect = loadImage("cloud1.png")

    def draw(self):
        Game.screen.blit(self.img, self.rect)

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        super().__init__(title, bg, fps)
        self.clouds = []
        for i in range(10):
            cloud = Cloud()
            cloud.rect.topleft = random_point()
            self.clouds.append(cloud)
        self.speed = 5
        self.index = 0
    
    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        for i in range(10):
            self.clouds[i].rect.left -= self.speed
            self.clouds[i].draw()
            if self.clouds[i].rect.left <0:
                self.clouds[i].rect.left = Game.width 

        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()