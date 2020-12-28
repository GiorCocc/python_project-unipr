ARENA_W, ARENA_H = 480, 360


class HeroBall:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._w = 20
        self._h = 20
        self._dx = 0
        self._dy = 0
        self._count=0

    def move(self):
        if self._count>0:
            self._x += self._dx
            self._y += self._dy
            self._count-=1

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def go_up(self):
        if self._count==0:
            self.count=5
            self._dx=0
            self._dy=-5

    def go_down(self):
        if self._count==0:
            self.count=5
            self._dx=0
            self._dy=5

    def go_right(self):
        if self._count==0:
            self.count=5
            self._dx=5
            self._dy=0

    def go_left(self):
        if self._count==0:
            self.count=5
            self._dx=-5
            self._dy=0


def main():
    # Create two objects, instances of the Ball class
    b1 = HeroBall(140, 180)

    for i in range(25):
        b1.move()
        print("b1 @", b1.position())

main()  # call main to start the program