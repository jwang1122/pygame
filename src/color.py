import pygame

pygame.init()
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Game Window")
BLACK=(0,0,0)
GRAY = (127, 127, 127)
WHITE = (255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0, 255, 255)
MAGENTA = (255,0,255)

bg = BLACK
key_dict = {pygame.K_k:BLACK, pygame.K_r:RED, pygame.K_g:GREEN, pygame.K_b:BLUE,
pygame.K_y:YELLOW, pygame.K_c:CYAN, pygame.K_m:MAGENTA, pygame.K_w:WHITE}

def paint():
    global bg
    win.fill(bg)
    pygame.display.update()

def mainloop():
    global bg
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN:
                bg = key_dict.get(event.key)
                pygame.display.set_caption(f"background color is {bg}")
                # if event.key == pygame.K_r:
                #     bg = RED
                # if event.key == pygame.K_m:
                #     bg = MAGENTA
                # if event.key == pygame.K_c:
                #     bg = CYAN
        paint()
    pygame.quit()

if __name__ == '__main__':
    mainloop()