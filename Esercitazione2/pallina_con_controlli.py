ARENA_W, ARENA_H = 480, 360
g=0.4

class Ball:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w = 20
        self._h = 20
        self._dx = 5
        self._dy = 5

    def go_up(self):
        self._dy-=5
    def go_down(self):
        self._dy=+5
    def go_left(self):
        self._dx-=5
    def go_right(self):
        self._dx+=5
    

    def multiple_moves(self, times:int):
        for i in range(times):
            self.move()

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy
        if keyboard.is_pressed("w"):
            self._dy=self.go_up()
        if keyboard.is_pressed("a"):
            self._dy=self.go_down()
        if keyboard.is_pressed("s"):
            self._dy=self.go_left()
        if keyboard.is_pressed("d"):
            self._dy=self.go_right()

        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h


def main():
    # Create two objects, instances of the Ball class
    b1 = Ball(140, 180)

    for i in range(25):
        b1.move()

main()  # call main to start the program


