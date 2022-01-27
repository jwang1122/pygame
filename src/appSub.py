from appSuper import *

class App(AppSuper):
    def paint(self):
        self.screen.fill(self.bg)
        pygame.draw.circle(App.screen,(255,0,0),(200,200), 100)
        pygame.display.update()

if __name__ == '__main__':
    App("My new title").mainloop()
