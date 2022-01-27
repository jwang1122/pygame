import pygame
from pygame.locals import *

BLACK=(0,0,0)
GRAY = (127, 127, 127)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
MAGENTA = (255,0,255)

class Text:
    def __init__(self, screen, text, pos, fontname='Arial Bold', fontsize=60, fontcolor=(0,0,0)):
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

class App:
    scenes = []
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        App.screen = pygame.display.set_mode((640, 240), flags)
        App.t = Text(App.screen, 'Pygame App', pos=(20, 20))
        App.running = True
    
    def run(self):
        """Run the main event loop."""
        while App.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    App.running = False
                self.handle(event)
            self.draw()
            pygame.display.update()
        pygame.quit()

    def handle(self, event):
        pass

    def draw(self):
        App.screen.fill(Color('gray'))
        App.t.draw()

class Scene:
    id=0
    bg = GRAY

    def __init__(self, caption="PyGame", bg=GRAY):
        pygame.display.set_caption(caption)
        App.scenes.append(self)
        App.scene = self
        self.id = Scene.id
        Scene.id +=1
        self.nodes = []
        self.bg = bg
                
    def draw(self):
        App.screen.fill(self.bg)
        for node in self.nodes:
            node.draw()
        pygame.display.flip()

    def __str__(self):
        return 'Scene {}'.format(self.id)

class Demo(App):
    def __init__(self):
        super().__init__()
        s0 = Scene(bg=CYAN)
        s0.nodes.append(Text(App.screen, 'Scene 0',(20, 20), fontsize=25))
        s0.nodes.append(Text(App.screen, 'the app introduction screen',(20,50)))
        s1 = Scene(bg=Color('yellow'))
        s1.nodes.append(Text(App.screen, 'Scene 1',(20,20), fontsize=25))
        s1.nodes.append(Text(App.screen, 'the app option screen',(20,50)))
        s2 = Scene(bg=Color('green'),caption='Introduction of Scene',)
        s2.nodes.append(Text(App.screen, 'Scene 2',(20,20), fontsize=25))
        s2.nodes.append(Text(App.screen, 'the app main screen',(20,50)))
        App.scene = App.scenes[0]

    def handle(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                App.scene = App.scenes[0]
            if event.key == pygame.K_b:
                App.scene = App.scenes[1]
            if event.key == pygame.K_c:
                App.scene = App.scenes[2]

    def draw(self):
        App.scene.draw()

if __name__ == '__main__':
    Demo().run()
