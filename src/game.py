from appsuper import *

class Game(AppSuper):
    def __init__(self, title="PyGame", bg=(255,255,0), fps=30):
        super().__init__(title, bg, fps)
        print(Game.screen.get_size())

    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()