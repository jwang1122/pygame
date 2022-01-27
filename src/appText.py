from appSuper import *

class App(AppSuper):
    def paint(self):
        # pygame.display.set_caption("My new title")
        # self.bg = (255, 255, 255)
        # self.screen.fill(self.bg)
        Text(AppSuper.screen, "Hello world!", (100,100), fontcolor=(0,255,0)).draw()
        text = Text(AppSuper.screen, "Welcome to PyGame!",(100, 180),"curlz", 30, (255,0,0))
        text.draw()
        text.setPos((50, 220)).draw()
        text.setPos((50, 250)).setFont(fontcolor=(200,234,122)).draw()
        
        pygame.display.update()

class Text:
    def __init__(self, screen, text, pos, fontname='Arial Bold', fontsize=72, fontcolor=(0,0,0)):
        self.text = text
        self.pos = pos
        self.screen = screen
        self.setFont(fontname, fontsize, fontcolor)
        self.render()

    def setFont(self, fontname='Arial Bold', fontsize=72, fontcolor=(0,0,0)):
        """Set the Font object from name and size."""
        self.fontname = fontname
        self.fontsize = fontsize
        self.fontcolor = fontcolor
        self.font = pygame.font.SysFont(fontname, fontsize)
        self.render()
        return self

    def setPos(self, pos):
        self.pos = pos
        self.render()
        return self

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        self.screen.blit(self.img, self.rect)

if __name__ == '__main__':
    App().mainloop()
