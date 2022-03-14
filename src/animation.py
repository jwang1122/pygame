from appsuper import *

class Mario(AppSuper):
    def __init__(self, title="Mario", bg=(127,127,127), fps=10):
        super().__init__(title, bg, fps)
        self.images = []
        img, rect = loadImage("run/1.png")
        self.images.append((img, rect))        
        img, rect = loadImage("run/2.png")
        self.images.append((img, rect))
        img, rect = loadImage("run/3.png")
        self.images.append((img, rect))
        img, rect = loadImage("run/4.png")
        self.images.append((img, rect))        
        img, rect = loadImage("run/5.png")
        self.images.append((img, rect))        
        img, rect = loadImage("run/6.png")
        self.images.append((img, rect))    
        self.index = 0
        self.rect = rect

    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type==KEYDOWN:
            if event.key in Mario.arrowKeys:
                self.rect.move_ip(Mario.arrowKeys[event.key])


    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.index += 1
        if self.index > 5:
            self.index = 0
        img, rect = self.images[self.index]
        self.screen.blit(img, self.rect)
        pygame.display.update()

if __name__ == '__main__':
    Mario().mainloop()