from appsuper import *

class Fist():
    def __init__(self):
        self.img, self.rect = loadImage("fist1.png", 0.025)
        self.fistSud = loadSound("whiff.wav")
        self.offset = (-10, 10)
        self.punching = False

    def playSound(self):
        self.fistSud.play()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft=pos
        self.rect.move_ip(self.offset)

    def punch(self, target):
        if not self.punching:
            self.punching = True
            hitbox=self.rect.inflate(-5, -5)
            return hitbox.colliderect(target)

    def unpunch(self):
        self.punching = False

    def draw(self):
        self.update()
        HitChimp.screen.blit(self.img, self.rect)

class Chimp():
    def __init__(self):
        self.img, self.rect = loadImage("chimp.png", 0.5)
        self.moving = False
        self.angle = 0
        self.original = self.img
        self.dizzy = False
        self.xSpeed = 5
        self.ySpeed = 5
        self.head = pygame.Rect(self.rect.left+110, self.rect.top+40, 50, 70)

    def update(self):
        if self.dizzy:
            self.rollover()
        else:
            self.walk()

    def draw(self):
        self.walk()
        if self.dizzy:
            self.rollover()
        HitChimp.screen.blit(self.img, self.rect)
        # pygame.draw.rect(HitChimp.screen, (255,0,0), self.head, 2)

    def rollover(self):
        center = self.rect.center
        self.angle += 12
        if self.angle >= 360:
            self.dizzy = False
            self.angle = 0
            self.img = self.original
        else:
            self.img = pygame.transform.rotate(self.original, self.angle)
        self.rect = self.img.get_rect(center = center)

    def walk(self):
        self.rect.left += self.xSpeed
        self.rect.top += self.ySpeed
        if self.rect.left < 0 or self.rect.right > HitChimp.width:
            self.xSpeed = -self.xSpeed
        if self.rect.top <0 or self.rect.bottom > HitChimp.height:
            self.ySpeed = -self.ySpeed
        self.head.topleft=(self.rect.left+110, self.rect.top+40)
        
class HitChimp(AppSuper):
    def __init__(self):
        super().__init__()
        self.sound = loadSound('yunque.mp3')
        self.sound.play(-1)
        self.chimp = Chimp()
        self.fist = Fist()
        self.bg, rect = loadImage('forest1.jpg')
        
        self.xSpeed = 5
        self.ySpeed = 5


    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.fist.punch(self.chimp.head):
                self.fist.playSound()
                self.chimp.dizzy = True
        elif event.type==pygame.MOUSEBUTTONUP:
            self.fist.unpunch()

    def drawLabel(self):
        drawText("Missing: ", (10, 10), (255,255,255))
        drawText("Hits: ", (400, 10), (255,255,255))

    def paint(self): # leave this function for subclass to implement
        self.screen.blit(self.bg, (0,0))

        self.drawLabel()
        self.chimp.draw()
        self.fist.draw()
        
        pygame.display.update()


if __name__ == '__main__':
    HitChimp().mainloop()