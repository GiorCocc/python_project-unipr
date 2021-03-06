#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

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
        self._g=0.4

    def multiple_moves(self, times:int):
        for i in range(times):
            self.move()

    def move(self):
        g=0.5
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy
        else:
            self._dy+=g

        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h


def main():
    # Create two objects, instances of the Ball class
    b1 = Ball(140, 180)
    b2 = Ball(180, 140)

    for i in range(25):
        b1.move()
        b2.move()
        print("b1 @", b1.position(), "b2 @", b2.position())

main()  # call main to start the program