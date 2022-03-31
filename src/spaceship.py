from appsuper import *

class MainFrame(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=60):
        super().__init__(title, bg, fps)
        self.spaceship = Spaceship()
    
    def handleEvent(self, event): 
        if event.type==KEYDOWN:
            if event.key in self.arrowKeys:
                self.spaceship.move(self.arrowKeys[event.key])
            if event.key == K_SPACE:
                self.spaceship.fire()

    def paint(self):
        self.screen.fill(self.bg)
        self.spaceship.draw()
        pygame.display.update()

class Bullet:
    def __init__(self, spaceship) -> None:
        self.sound = loadSound('whiff.wav')
        self.bullet = pygame.Rect(0,0,15,5)
        self.spaceship = spaceship
        self.bullet.center = spaceship.rect.center
        self.isFire = False
        self.speed = (5,0)

    def draw(self):
        if self.isFire:
            self.bullet.move_ip(self.speed)
            if self.bullet.right>MainFrame.width:
                self.bullet.center = self.spaceship.rect.center
                self.isFire = False
        pygame.draw.rect(MainFrame.screen, MainFrame.BLACK, self.bullet)

    def move(self, speed):
        self.bullet.move_ip(speed)

    def fire(self):
        self.isFire = True
        self.sound.play()

class Spaceship:
    def __init__(self) -> None:
        self.img, self.rect = loadImage('spaceship.png', 0.2)
        self.bullet = Bullet(self)
        self.speed = (5,0)
    
    def draw(self):
        MainFrame.screen.blit(self.img, self.rect)
        self.bullet.draw()
    
    def fire(self):
        self.bullet.fire()

    def move(self, speed):
        self.rect.move_ip(speed)
        self.bullet.move(speed)

if __name__ == '__main__':
    MainFrame("Spaceship").mainloop()