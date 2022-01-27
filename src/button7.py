from myapp import *

class Button(pygame.Rect):
    """
    This class takes the x-position and the y-position, width and height of an image.
    """
    def __init__(self, x, y, width, height, image, hover_image=None):
        super().__init__(x, y, width, height)
        self.image = image
        self.hover_image = hover_image

    def update(self, screen, mouse_pos=None):
        if self.hover_image is not None \
        and mouse_pos is not None \
        and self.collidepoint(mouse_pos):
            screen.blit(self.hover_image, (self.x, self.y, self.w, self.h))
        else:
            screen.blit(self.image, (self.x, self.y, self.w, self.h))

class Demo(App):
    def __init__(self, title="Button Test", bg=CYAN, fps=60):
        super().__init__(title, bg, fps)
        font = pygame.font.SysFont('Arial Bold', 25)    
        img = font.render("Click Me", False, WHITE, MAGENTA)
        imghover = font.render("Click Me", False, BLACK, YELLOW)
        self.button = Button(10,10, 50, 30, img, imghover)
        self.mousePos = None

    def paint(self):
        App.screen.fill(self.bg)
        pos = pygame.mouse.get_pos()
        self.button.update(App.screen, pos)
        pygame.display.flip()

if __name__ == '__main__':
    Demo().mainloop()