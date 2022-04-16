from appsuper import *

class Player:
    def __init__(self, enemies):
        self.enemies = enemies
        self.img, self.rect = loadImage('fighterJet2.png')
        self.misle = Rect(0,0,10,3)
        self.misle.center = self.rect.center
        self.fire = False
        self.gameOver = False
        self.xSpeed = 50
        self.ySpeed = 5

    def draw(self):
        if self.rect.left >= Game.width:
            self.gameOver = True
            self.img, self.rect = loadImage('win2.png')
            self.rect.topleft = (220, 160)
            self.xSpeed = 0
        if not self.gameOver:
            self.rect.top += self.ySpeed
            if not self.fire:
                self.misle.center = self.rect.center
            else:
                self.misle.move_ip(20, 0)
                if self.misle.left >= Game.width:
                    self.fire = False
                for enemy in self.enemies:
                    if self.misle.colliderect(enemy):
                        self.enemies.remove(enemy)
                        self.fire = False

        Game.screen.blit(self.img, self.rect)
        pygame.draw.rect(Game.screen,Game.BLACK,self.misle)

    def move(self, direction):
        if(direction==Game.RIGHT):
            self.rect.move_ip((self.xSpeed, 0))
        elif direction==Game.LEFT:
            self.rect.move_ip((-self.xSpeed, 0))
        elif direction==Game.UP:
            self.ySpeed = -5
        else:
            self.ySpeed = 5
        
class Enemy:
    def __init__(self):
        self.img, self.rect = loadImage('fighter4.png')
        self.enemies = randomRects(10, 40, 30)
        self.speed = (-10, 0)

    def draw(self):
        for i in range(len(self.enemies)):
            rect = self.enemies[i]
            rect.move_ip(self.speed)
            if rect.right<0:
                rect.left = Game.width
            Game.screen.blit(self.img, rect)

class Cloud:
    def __init__(self) -> None:
        self.cloudImg, self.rect = loadImage("cloud1.png")
        self.clouds = randomRects(10, 50, 30)
        self.speed = (-3,0)
    
    def draw(self):
        for i in range(len(self.clouds)):
            rect = self.clouds[i]
            rect.move_ip(self.speed)
            if rect.right<0:
                rect.left = Game.width
            Game.screen.blit(self.cloudImg, rect)

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        self.openFire = loadSound("whiff.wav")
        super().__init__(title, bg, fps)
        self.cloud = Cloud() 
        self.enemy = Enemy()
        self.player = Player(self.enemy.enemies)

    def handleEvent(self, event): # leave this funself.cloud tion for subself.cloud lass to implement
        if event.type==KEYDOWN:
            if event.key in self.directions:
                self.player.move(self.directions[event.key])
            if event.key == K_SPACE:
                self.player.fire = True
                self.openFire.play()

    def paint(self): # leave this funself.cloud tion for subself.cloud lass to implement
        self.screen.fill(self.bg)
        self.cloud.draw()
        self.enemy.draw()
        self.player.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()    