<h1>Python Game Learning Notes</h1>

Click to see website: [PyGame Document](https://www.pygame.org/docs/)

[PDF doc](https://buildmedia.readthedocs.org/media/pdf/pygame/latest/pygame.pdf)

[Download sounds](https://freesound.org/people/adh.dreaming/sounds)

[memory Game](https://www.youtube.com/watch?v=KAn1f16Cl1I)

[Jump Game ](https://www.youtube.com/watch?v=AY9MnQ4x3zk)

[Space Invaders](https://www.youtube.com/watch?v=Q-__8Xw9KTM)

[Program Arcade Games](http://programarcadegames.com/index.php?chapter=example_code)

[Physics Simulations](https://www.youtube.com/watch?v=tLsi2DeUsak)


📌 pip: Package Installer for Python
preferred installer program

```
python -m venv env
python.exe -m pip install --upgrade pip
pip install pygame
```

😢❌ Warning: Python 11.0 does not support pygame-2.1.2

❓ What is pygame?

✔️ Pygame is a multimedia library for Python for making games and multimedia applications.

❓ What is Surface?
✔️ pygame object for representing images.  

❓ what is blit()?
✔️ blit() — blit stands for Block Image Transfer — and it's going to copy the contents of one Surface onto another Surface . The two surfaces in question are the screen that you created and the new Surface. blit() will take that rectangular Surface and put it on top of the screen.

❓ what is flip()?

✔️ flip() updates the entire Surface on the display. pygame. display. update() updates the entire Surface, only if no argument is passed.

❓ what is move_ip() for?

✔️ The move_ip() stands for move in-place, which means we move the rectangle relative to its previous position.

- [create main surface.](#create-main-surface)
- [create main loop](#create-main-loop)
- [add time tick](#add-time-tick)
- [images](#images)
- [color](#color)
- [Bounced Ball](#bounced-ball)
- [Draw Text](#draw-text)
- [Draw Shapes](#draw-shapes)
- [Use class](#use-class)
- [Making sounds](#making-sounds)
- [Collision](#collision)
- [Fight Chimp](#fight-chimp)
- [Yahtzee Dice Game](#yahtzee-dice-game)
- [Fire Bullets](#fire-bullets)
- [Button](#button)
- [Draw Shapes](#draw-shapes-1)
- [animation](#animation)
- [Sample games](#sample-games)
- [Snake Eat Apple](#snake-eat-apple)
- [Space Invaders](#space-invaders)
- [Image Font](#image-font)
- [2D Game Categorization](#2d-game-categorization)
- [Online Game](#online-game)
- [References](#references)

```mermaid
graph TB
A(PyGame)
B([Event Loop<br>Handle User Actions])
C([Main Loop])
D[time tick]
E[Display Update]
F["Game Over<br>pygame.quit()"]
I["Initialize<br>pygame.init()"]

A-->I-->C-->D-->B-->E
E-->C
B-->F

classDef start fill:green,stroke:#096125,stroke-width:4px,color:white;
classDef process fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;
classDef loop fill:#6CB4F2,stroke:black,stroke-width:1px;
classDef end1 fill:red,stroke:#840F45,stroke-width:4px,color:white;

class C start
class D,E,I process
class B loop
class F end1
```
## create main surface.

```py
WIDTH, HEIGHT = 900, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
```
Click to see source code: [open a window](../src/openWindow.py)

## create main loop
it will keep window open

```py
def mainloop():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
    
    pygame.quit()

if __name__ == '__main__':
    main()
```

## add time tick

```py
clock = pygame.time.Clock()
clock.tick(1) #FPS: 1 frame per second
```
Click to see source code: [Time tick](../src/timeTick.py)


## images
* [Load Image, resize, rotate](../src/loadImage.py)
```py
YELLO_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
```
* [](../src/main.py)
* [load and display image](../src/loadImage2.py)
* [loadImage(), scale and move image](../src/loadImage3.py)
* [Move Image](../src/moveImage.py)
* [Move image with muse](../src/image1.py)
* [rotate, change size of image](../src/image2.py)

❓ What is Surface?
✔️ surfaces are generally used to represent the appearance of the object and its position on the screen. All the objects, text, images that we create in Pygame are created using surfaces.

❓ What is flip()?
✔️ display.flip() will update the contents of the entire display

❓ What is update()?
✔️ display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display. display.update() is faster in most cases.

❓ What is blit()?
✔️blit stands for Block Image Transfer—and it's going to copy the contents of one Surface onto another Surface .

```py
pygame.display.set((w, h), pygame.DOUBLEBUF)
```

## color
Click to see source code: [Background color](../src/color.py)

## Bounced Ball
* [Bounced Ball](../src/ball.py)

## Draw Text
* [Draw Text](../src/drawText.py)
* [Editable Text](../src/editText.py)
* [PyGame Coordinates](../src/coordinates.py)
* [display text](../src/myapp.py)

## Draw Shapes
* [draw line](../src/drawLine.py)
* [draw arc](../src/drawArc.py)
* [draw circle](../src/drawCircle.py)
* [common function for rectangle](../src/rect.py)
* [](../src/multipleRect.py)
  
🔑⚡️ **Knowlodge Base:**
1. get moving speed based on arrow key from dict [](../src/rect4.py)
2. 2 way to create rect: Rect(x,y,w,h) or Rect(pos, size)
3. to draw text(a. create font; b. create Surface; c. blit on screen)
```py
def draw_text(text, pos):
    font = pygame.font.SysFont('Arial Bold', 25)    
    img = font.render(text, True, BLACK)
    screen.blit(img, pos)
```
💡👉 screen.blit(img, rect) works the same way.

* [Draw Rectangle](../src/drawRectangle.py)
* [Draw Eclipses, catch mouse actions](../src/drawEllipses.py)
* [](../src/drawShaps.py)
* [use mouse draw shape](../src/mouse4.py)
* [](../src/mouseDraw.py)
* 
* [draw rectagle on screen](../src/rect1.py)
* [Special points of rectangle](../src/rect2.py)
* [change rectangle location by key](../src/rect3.py)
* [move_ip() move rectangle by arrow keys](../src/rect4.py)
* [inflate_ip() change rect size](../src/rect5.py)
* [clip(), union()](../src/rect6.py)
* [event.pos, event.rel](../src/rect7.py)
* [event bounced rectangle](../src/rect8.py)

## Use class
* [Super class](../src/appSuper.py)
* [Subclass](../src/appSub.py)
* [Text class](../src/appText.py)
* [My App Super class](../src/myapp.py)
* [Scene class, different frames](../src/scene.py)
* [Game class](../src/game.py)

  
## Making sounds
[wav, mp3](../src/sound1.py)

## Collision
* [collidepoint(), randompoints()](../src/rect9.py)
* [colliderect(), randomrects()](../src/rect10.py)
* [colliderect(), red collisioned](../src/rect11.py)
* [colliderect(), arrow key collision](../src/rect20.py)
* [Understand Collision, large image, small hit area](../src/rect21.py)
* [hit chimp head](../src/rect22.py)

## Fight Chimp
* [Display Chimp image](../src/displayChimp.py)
* [move chimp on screen](../src/moveChimp.py)
* [mouse Fist](../src/mouseFist.py)
* [](../src/chimprollover.py)
* [mouse click punch sound](../src/fistPunch.py)
* [](../src/fistHitChimp.py)
* [OOP design](../src/FistRolloverChimp.py)
* [add Text on Screen](../src/appText.py)
* [Choose Font](../src/font1.py)
* [add score missing, and hit](../src/FistRolloverChimp.py)
* [add score missing, and hit](../src/FistRolloverChimp1.py)
* [add background]()

## Yahtzee Dice Game
* [dice rotate](../src/dice.py)

[Yahtzee dice game](Yahtzee.pdf)

## Fire Bullets
* [](../src/bullet.py)
* [](../src/bullet2.py)
* [fire missle](../src/rect23.py)
* [OOP arrow key control spaceship](../src/spaceship.py)

```mermaid
classDiagram

class Game{
    spaceship:Spaceship
    handleEvent()
    paint()
}
class Spaceship{
    image
    bullet:Bullet
    draw()
    fire()
    move()
}
class Bullet{
    rect:Rect
    isFire:bool
    draw()
    move()
    fire()
}

Spaceship *-- Bullet
MainFrame *--Spaceship
```
* [moving fighter](../src/fighter.py)
* [moving fighter with player](../src/fighter1.py)

* [Hit target]()

## Button
* [](../src/button1.py)
* [](../src/button2.py)
* [](../src/button3.py)
* [](../src/button4.py)
* [](../src/button5.py)
* [](../src/button6.py)
* [Button class extends Rect](../src/button7.py)

💡👉 Can get mouse position any time.

## Draw Shapes
* [Draw Line](../src/drawLine.py)
* [Draw Circle](../src/drawCircle.py)
* [Draw Arc](../src/drawArc.py)
* [Draw Ellipes](../src/drawEllipses.py)
* [Draw Polygon](../src/drawPolygon.py)


## animation
* [Super Mario](../src/animationMario.py)
* [animation Snow](../src/animation1.py)
* [Scene of game](../src/animationCloud.py)
* [block jump](../src/jump1.py)

![](physicsformular.jpg)

$$y = y_0 + v_{y_0} t - \frac 1 2 g t^2 $$

* [Jump formular](../src/jumpformular.py)
* [Stright-up jump](../src/jump2.py)
* [Forward jump](../src/jump3.py)
* [rect jump](../src/rectJumper.py)
* [](../src/scroller.py)
* [jump block](../src/blockMoving.py)

* [Change image size](../src/changeImage.py)

❓what is RGBA?
✔️ RGBA stands for red green blue alpha. While it is sometimes described as a color space, it is actually a three-channel RGB color model supplemented with a fourth alpha channel.

![](RGBA_comp.png)
Example of an RGBA image composited over a checkerboard background. alpha is 0% at the top and 100% at the bottom.

![](HexRGBAbits.png)

* [moving clouds](../src/clouds.py)
* [moving fighters](../src/fighter.py)
* [stop on rect](../src/moveblock.py)
* [](../src/moveWithWall.py)
* [walk around wall](../src/runner.py)

## Sample games
* [Fist and Chimp](../src/chimp.py)
* [Ping-Pong](../src/pong.py)
* [](../src/pong2.py)
* [](../src/spaceFight.py)
* [Game Base](../src/app.py)
* [space invaders](spaceInvaders.mp4)
* [walk around wall](../src/runner.py)

![](airfighter.gif)
![](smallFighter.png)
![](missle.png)

## Snake Eat Apple
* [snake](../snake/doc/snake.md)
* [](../src/snake.py)
* [Display Snake](../snake/src/snakeApple.py)
* [Snake move](../snake/src/snakeMove.py)
* [snake with long tail](../snake/src/snakeMoveVector.py)
* [snake eat apple](../snake/src/collision.py)
  
## Space Invaders
* [space invader](../SpaceInvaders/doc/spaceInvaders.md)

## Image Font
[ImageFont document](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html)
[Change Image](../src/changeImage.py)

```py
def createTransparentText(fileOut, text, /, width=150, height=30, *, color=(255, 255, 255, 0), mode='RGBA')
def createBullet(fileOut, /, width, height, *, color=(255, 255, 255, 0), mode='RGBA')
```

## 2D Game Categorization

```mermaid
graph TB

GAME([2D Games])
CHAR["Characters<br>(Fist)"]
OBJ["Objects<br>(Chimp)"]
ENV["Environment<br>(Background)"]
SOUND["Sound Effects"]
MOVE["Movement<br>(mouse or key controlled <br>time controlled)"]
SIDE[Side move]
ROLL[Vertical-Scrolling]
ANIM[Animation]

GAME --> CHAR & OBJ & ENV & MOVE & SOUND
MOVE --> SIDE & ROLL & ANIM

classDef start fill:#2DD276,stroke:#096125,stroke-width:4px,color:white;
classDef process fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;

class GAME start
class CHAR,OBJ,ENV,MOVE,SOUND process
```

* Role-Playing Games(RPG)
> More commonly known as RPG, role-playing games are games with a protagonist or hero who goes through different levels to improve their skills and defeat enemies. 
* Co-op Games
>Cooperative games, or commonly referred to as co-op games, bring players together often in the same setting. But instead of working against each other, as is the case for multiplayer games in general, players work as a group toward a common goal.
samples are: Castle Crashers, Terraria, Ninja Turtles...
* Run and Gun, Beat 'Em Ups, Hack and Slash
> Action-packed and built for fighting, these three types of games all have a similar flavor with some nuances.
* Platformers
> As the name suggests, platformers let players surmount obstacles and progress through levels by “[jumping] or [climbing] between different platforms on screen,” says STEM-oriented educational group iD Tech. 
* Puzzle Games
>Popular puzzle games are Unblock Me (2009), Candy Crush (2012), 2048 (2014), and You Must Build A Boat (2015). 

```mermaid
graph TB

GAME([2D Games])
FIGHT[Gun, Missle, fight]
PLAT[Platformer<br> scene, jump, treasure]
BOARD[Board Game<br>Chess, Poker, Domino, Dice]

GAME --> FIGHT & PLAT & BOARD
classDef start fill:#2DD276,stroke:#096125,stroke-width:4px,color:white;
classDef process fill:#F46624,stroke:#F46624,stroke-width:4px,color:white;

class GAME start
class FIGHT,PLAT,BOARD process
```
[2D Game design pattern](https://www.gamedeveloper.com/design/level-design-patterns-in-2d-games)
## Online Game
[pygame and socket](https://www.youtube.com/watch?v=McoDjOCb2Zo)
* [online game](../src/mysocket.py)

## References
[Working on Image](https://www.geeksforgeeks.org/working-images-python/)
[Popular 2D Games](https://narrasoft.com/what-are-the-different-types-of-2d-games/)