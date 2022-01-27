from myapp import *

class MyButton(App):
    def __init__(self):
        super().__init__("Button")
        self.btn1 = pygame.Button()

if __name__ == '__main__':
    MyButton().mainloop()