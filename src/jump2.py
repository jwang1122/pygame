from appsuper import *

class Mario():
    def __init__(self) -> None:
        self.top = 300
        self.width = 50
        self.bottom = self.top + self.width
        self.rect = pygame.Rect(10, self.top, 30,self.width)
        self.isJump = False
        self.t = 0
        self.tgap = 0.01

    def jump(self):
        if self.isJump:
            self.t += self.tgap
            deltY = jump(self.t, 0.49)
            self.rect.bottom = self.bottom - deltY
            if deltY<=0:
                self.rect.bottom = self.bottom
                self.t = 0
                self.isJump = False
                
    def forward(self):
        self.rect.left += 5

    def backward(self):
        self.rect.left -= 5

    def draw(self):
        if self.isJump:
            self.jump()
        pygame.draw.rect(Game.screen, Game.RED, self.rect)

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(0,255,255), fps=30):
        super().__init__(title, bg, fps)
        self.mario = Mario()

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type == KEYDOWN: 
            if event.key==K_SPACE:
                self.mario.isJump = True
            if event.key==K_RIGHT:
                self.mario.forward()
            if event.key==K_LEFT:
                self.mario.backward()


    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.mario.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game("Jump Demo").mainloop()