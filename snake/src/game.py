from appsuper import *

class Game(AppSuper):
    def handleEvent(self, event): # leave this function for subclass to implement
        pass

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()