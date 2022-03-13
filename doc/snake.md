<h1>Snake Eat Apple</h1>

## start up

[open game window](../snake/src/game.py)

```mermaid
classDiagram

class Game{
    apple:Apple
    snake:Snake
    paint()
    handleEvent()
}

class Apple{
    image:Image
    draw()
}

class Snake{
    head:Image
    tail:Image
    draw()
}

Game *-- Apple
Game *-- Snake
```

## display apple and snake
[display apple and snake](../snake/src/snakeApple.py)

## move snake
[move snake by key](../snake/src/snakeMove.py)

😢❌: do not allow snake goes backwards?

## collision
[](../snake/src/collision.py)