from random import randint
import g2d
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

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy
    
    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

def tick():
    g2d.clear_canvas()  # BG
    for b in balls:
        b.move()
        g2d.set_color(b.color())
        g2d.fill_rect(b.position())  # FG


balls = [ColoredBall(40, 80), ColoredBall(80, 40), ColoredBall(120, 120)]
g2d.init_canvas((ARENA_W, ARENA_H))
g2d.main_loop(tick)
