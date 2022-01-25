from appSuper import *

class Demo(AppSuper):
    def __init__(self):
        super().__init__()
        # print('init = ', pygame.mixer.get_init())
        # print('channels =', pygame.mixer.get_num_channels())
        AppSuper.snd = pygame.mixer.Sound('src/data/yunque.mp3')
        AppSuper.snd.play()     

if __name__ == '__main__':
    Demo().mainloop()