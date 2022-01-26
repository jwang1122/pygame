from rect import *
  
rect1 = pygame.Rect(20,20,20,20)
collisionSound = pygame.mixer.Sound('src/data/punch.wav')    
chimpImg = pygame.image.load('src/data/chimp.png')
chimpImg = pygame.transform.scale(chimpImg, (300,400))
gap = 40
rect = chimpImg.get_rect()
while running:
    head = Rect(rect.left+150, rect.top+40, 80, 110)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect1.move_ip(v)
                if rect1.colliderect(head):
                    collisionSound.play()
            if event.key==pygame.K_SPACE:
                rect.move_ip(10,10)
                if rect1.colliderect(head):
                    collisionSound.play()
            if event.key==pygame.K_LCTRL:
                rect.move_ip(-10,-10)
                if rect1.colliderect(head):
                    collisionSound.play()
    screen.fill(GRAY)
    screen.blit(chimpImg, rect)
    pygame.draw.rect(screen, GREEN, rect, 2)
    pygame.draw.rect(screen, GREEN, rect1, 1)
    pygame.draw.rect(screen, GREEN, head, 1)
    pygame.display.flip()
pygame.quit()