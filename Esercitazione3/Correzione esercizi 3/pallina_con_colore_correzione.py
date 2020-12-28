#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''
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
        r=(randint(0,256))
        g=(randint(0,256))
        b=(randint(0,256))
        self._color=(r,g,b)

    def multiple_moves(self, times:int):
        for i in range(times):
            self.move()

    def move(self):
        if not (0 <= self._x + self._dx <= ARENA_W - self._w):
            self._dx = -self._dx
        if not (0 <= self._y + self._dy <= ARENA_H - self._h):
            self._dy = -self._dy

        self._x += self._dx
        self._y += self._dy

    def position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def color(self) -> (int, int, int):
        return self._color
