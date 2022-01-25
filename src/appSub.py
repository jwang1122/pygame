from appSuper import *

class App(AppSuper):
    def paint(self):
        pygame.display.set_caption("My new title")
        self.bg = (255, 255, 255)
        self.screen.fill(self.bg)
        pygame.display.update()

if __name__ == '__main__':
    App()
