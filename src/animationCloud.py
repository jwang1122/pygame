from appsuper import *

class Scene(AppSuper):
    def __init__(self, title="Mario", bg=(87,173,247), fps=10):
        super().__init__(title, bg, fps)
        loadSound("yunque.mp3").play(-1)
        self.tile, self.tileRect = loadImage("terrain_tiles.png")
        self.tileRect.bottom = 500
        self.tileRect.left = Scene.width
        self.images = []
        img, rect = loadImage("clouds/1.png")
        self.images.append((img, rect))        
        img, rect = loadImage("clouds/2.png")
        self.images.append((img, rect))
        img, rect = loadImage("clouds/3.png")
        self.images.append((img, rect))
        self.index = 0
        self.rect = rect
        self.rect.left =Scene.width
        self.speed = 10
        self.tileSpeed = 4


    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.index += 1
        if self.index > len(self.images)-1:
            self.index = 0
        img, rect = self.images[self.index]
        self.rect.left -= self.speed
        if self.rect.left<-Scene.width:
            self.rect.left = Scene.width 
        self.screen.blit(img, self.rect)
        self.tileRect.left -= self.tileSpeed
        if self.tileRect.left<-self.tileRect.width+50:
            self.tileRect.left=Scene.width
        self.screen.blit(self.tile, self.tileRect)
        pygame.display.update()

if __name__ == '__main__':
    Scene().mainloop()