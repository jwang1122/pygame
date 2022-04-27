from appsuper import *

class Apple:
    def __init__(self):
        self.image, self.rect = loadImage("apple3.png")
        self.next()
    
    def draw(self):
        Game.screen.blit(self.image, self.rect)

    def next(self):
        self.rect.topleft = randomPoint()

class Snake:
    def __init__(self, apple):
        self.apple = apple
        self.head, self.rectHead = loadImage("head.png")
        self.body, self.rectBody = loadImage("body.jpg")
        self.speed = (0, 40)
        self.rectHead.move_ip(0, 80)
        self.rectBody.move_ip(0, 40)
        self.bodies = [] # bodies holds rects for snake where index=0 is the head
        self.bodies.append(self.rectHead)
        self.bodies.append(self.rectBody)
        self.bodies.append(Rect(0,0,40,40))
    
    def draw(self):
        self.move()
        Game.screen.blit(self.head, self.bodies[0])
        for i in range(1,len(self.bodies)):
            Game.screen.blit(self.body, self.bodies[i])

    def move(self):
        for i in range(len(self.bodies)-1, 0, -1): # simulate snake moving
            self.bodies[i] = self.bodies[i-1]
        head = Rect(self.bodies[0])
        head.move_ip(self.speed)
        self.bodies[0] = head

        # figure out if the head hit the apple
        if head.colliderect(self.apple.rect):
            self.bodies.append(Rect(-40,-40,40,40)) # initial position is not important
            self.apple.next()

        for i in range(2, len(self.bodies)-1): 
            if head.colliderect(self.bodies[i]): # hit its body
                Game.gameover = True

        if head.bottom > Game.height or head.top <0 or head.left <0 or head.right > Game.width:
            print("Game Over!!!")
            Game.gameover = True

class Game(AppSuper):
    gameover = False
    def __init__(self, title="PyGame", bg=(0,255,255), fps=3):
        super().__init__(title, bg, fps)
        self.apple = Apple()
        self.snake = Snake(self.apple)


    def handleEvent(self, event): # leave this function for subclass to implement
        if event.type == KEYDOWN and event.key in self.speeds:
            self.snake.speed = self.speeds[event.key]

    def paint(self): # leave this function for subclass to implement
        self.screen.fill(self.bg)
        if not Game.gameover:
            self.snake.draw()
            self.apple.draw()
        pygame.display.update()

if __name__ == '__main__':
    Game().mainloop()    