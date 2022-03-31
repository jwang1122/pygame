from appsuper import *

class Scene(AppSuper):
    def __init__(self, title="Mario", bg=(87,173,247), fps=10):
        super().__init__(title, bg, fps)
        # loadSound("yunque.mp3").play(-1)
        self.landscape = []
        tile, rect = loadImage("terrain_tiles.png")
        rect.bottom = 500
        rect.left = Scene.width
        self.landscape.append((tile,rect))
        tile, rect = loadImage("terrain_tiles.png",0.5)
        rect.bottom = 500
        rect.left = Scene.width + 380
        self.landscape.append((tile, rect))
        self.tileIndex = 0



        self.clouds = []
        img, rect = loadImage("clouds/1.png")
        self.clouds.append((img, rect))        
        img, rect = loadImage("clouds/2.png")
        self.clouds.append((img, rect))
        img, rect = loadImage("clouds/3.png")
        self.clouds.append((img, rect))
        self.cloudsIndex = 0
        self.rect = rect
        self.rect.left =Scene.width
        self.speed = 10
        self.tileSpeed = 4


    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        self.drawCloud()
        self.drawTitle()
        pygame.display.update()

    def drawTitle(self):
        for tile in self.landscape:
            if tile[1].left < -300:
                tile[1].left = Scene.width

            tile[1].left -= self.speed
            self.screen.blit(tile[0], tile[1])


    def drawCloud(self):
        self.cloudsIndex += 1
        if self.cloudsIndex > len(self.clouds)-1:
            self.cloudsIndex = 0
        img, rect = self.clouds[self.cloudsIndex]
        self.rect.left -= self.speed
        if self.rect.left<-Scene.width:
            self.rect.left = Scene.width 
        self.screen.blit(img, self.rect)

if __name__ == '__main__':
    Scene().mainloop()