from rect import *
  
rect1 = pygame.Rect(20,20,20,20)
collisionSound = pygame.mixer.Sound('src/data/punch.wav')    
img = pygame.image.load('src/data/Gold-Medal.gif')
img = pygame.transform.scale(img, (300,300))
gap = 40
rect = img.get_rect()
rect2 = Rect(rect.left+gap, rect.top+gap, rect.width-2*gap, rect.height-2*gap)
# rect = Rect(rect.left+10, rect.right-10, rect.width-20, rect.height-20)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect1.move_ip(v)
                if rect1.colliderect(rect2):
                    collisionSound.play()
    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect, 2)
    pygame.draw.rect(screen, GREEN, rect1, 1)
    pygame.draw.rect(screen, GREEN, rect2, 1)
    screen.blit(img, rect)
    pygame.display.flip()
pygame.quit()