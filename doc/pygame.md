<h1>Python Game Learning Notes</h1>

Click to see website: [PyGame Document](https://www.pygame.org/docs/)

[PDF doc](https://buildmedia.readthedocs.org/media/pdf/pygame/latest/pygame.pdf)

[Download sounds](https://freesound.org/people/adh.dreaming/sounds)

[memory Game](https://www.youtube.com/watch?v=KAn1f16Cl1I)

[Jump Game ](https://www.youtube.com/watch?v=AY9MnQ4x3zk)

📌 pip: Package Installer for Python
preferred installer program

❓ What is pygame?

✔️ Pygame is a multimedia library for Python for making games and multimedia applications.

- [create main surface.](#create-main-surface)
- [create main loop](#create-main-loop)
- [add time tick](#add-time-tick)
- [load image](#load-image)
- [move the images](#move-the-images)
- [color](#color)
- [Bounced Ball](#bounced-ball)
- [Draw Shapes](#draw-shapes)
- [Use class](#use-class)
- [Making sounds](#making-sounds)

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
[open a window](../src/openWindow.py)

## create main loop
it will keep window open

```py
def main():

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
[](../src/timeTick.py)

## load image

[Load Image, resize, rotate](../src/loadImage.py)
```py
YELLO_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
```

## move the images
[Move Image](../src/moveImage.py)

## color
[Background color](../src/color.py)

## Bounced Ball
[Bounced Ball](../src/ball.py)

## Draw Shapes
* [Draw Rectangle](../src/rectangle.py)
* [Draw Eclipses, catch mouse actions](../src/ellipses.py)

## Use class
* [Super class](../src/appSuper.py)
* [Subclass](../src/app.py)
* [Text class](../src/appText.py)
  
## Making sounds
[wav, mp3](../src/sound1.py)