from rect import *
  
rect1 = pygame.Rect(60,30,30,30)
rect2 = pygame.Rect(20,20,20,20)
collisionSound = pygame.mixer.Sound('src/data/punch.wav')    

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect1.move_ip(v)
                if rect1.colliderect(rect):
                    collisionSound.play()
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 1)
    pygame.draw.rect(screen, GREEN, rect1, 1)
    pygame.draw.rect(screen, GREEN, rect2, 1)
    pygame.display.flip()
pygame.quit()