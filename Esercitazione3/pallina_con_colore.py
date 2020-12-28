from random import randint
ARENA_W, ARENA_H = 480, 360

class ColoredBall:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w = 20
        self._h = 20
        self._dx = 5
        self._dy = 5
        self._r = randint(0,256)
        self._g = randint(0,256)
        self._b = randint(0,256)
    
    def color(self) ->(int, int, int):
        return self._r, self._g,self._b


def main():
    b = ColoredBall(140, 180)
    print("b colore:", b.color())

main()