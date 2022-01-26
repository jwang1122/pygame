from rect import *
  
fireSound = pygame.mixer.Sound('src/resources/whiff.wav')    
shipImg = pygame.image.load('src/resources/spaceship.png')
shipImg = pygame.transform.scale(shipImg, (300,300))
gap = 40
rect = shipImg.get_rect()
rect1 = pygame.Rect(rect.midright[0]-80,rect.midright[1],20,10)

fire = False
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key==pygame.K_SPACE and not fire:
                rect1 = pygame.Rect(rect.midright[0]-80,rect.midright[1],20,10)
                fireSound.play()
                fire = True
    if rect1.left<width and fire:
        print(rect1.left)
        rect1.move_ip(20,0)
    else:
        fire = False
    screen.fill(GRAY)
    screen.blit(shipImg, rect)
    pygame.draw.rect(screen, GREEN, rect, 2)
    pygame.draw.rect(screen, BLACK, rect1, 0)
    pygame.display.flip()
pygame.quit()