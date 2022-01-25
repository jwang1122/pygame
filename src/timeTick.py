import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fight")

WHITE = (255,255,255)
FPS = 1

def drawWindow(count):
    WIN.fill(WHITE)
    print(f"update Window...{count}")
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    count = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
        count += 1
        drawWindow(count)
    pygame.quit()

if __name__ == '__main__':
    main()