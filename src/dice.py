from myapp import *

class Dice:
    def __init__(self, img, rect, value, pos=(0, 0)):
        self.image = img
        self.rect = rect
        self.value = value
        self.pos = pos
        self.isRoll = False
        self.original = self.image
    
    def display(self):
        if self.isRoll:
            self.spin()
        App.screen.blit(self.image, self.pos)

    def spin(self):
        """spin the dice image"""
        center = self.rect.center
        self.isRoll = self.isRoll + 12
        if self.isRoll >= 720:
            self.isRoll = False
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.isRoll)
        self.rect = self.image.get_rect(center=center)

    def thrown(self):
        if not self.isRoll:
            self.isRoll = True
            self.original = self.image

class Demo(App):
    def __init__(self, title="Python Game", bg=CYAN, fps=60):
        super().__init__(title, bg, fps)
        img, rect = loadImage('dice6red.png')
        self.dice = Dice(img, rect, 6, (100,100))

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.dice.thrown()

    def paint(self):
        App.screen.fill(WHITE)
        self.dice.display()
        pygame.display.update()

if __name__ == '__main__':
    Demo().mainloop()