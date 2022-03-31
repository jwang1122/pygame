from appsuper import *

class RolloverChimp(AppSuper):
    def __init__(self):
        super().__init__()
        self.chimpImg, self.chimpRect = loadImage("chimp.png", 0.5)
        self.angle = 1
        self.original = self.chimpImg
        self.dizzy = False

    def handleEvent(self, event):
        if event.type==MOUSEBUTTONDOWN and not self.dizzy:
            self.dizzy = True

    def rollover(self):
        center = self.chimpRect.center
        self.angle += 12
        if self.angle >= 360:
            self.dizzy = False
            self.angle = 0
            self.chimpImg = self.original
        else:
            self.chimpImg = pygame.transform.rotate(self.original, self.angle)
        self.chimpRect = self.chimpImg.get_rect(center = center)


    def paint(self):
        self.screen.fill(self.bg)
        if self.dizzy:
            self.rollover()
        RolloverChimp.screen.blit(self.chimpImg, self.chimpRect)
        pygame.display.update()

if __name__ == '__main__':
    RolloverChimp().mainloop()