#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import choice, randint


class Greatest(BoardGame):

    def __init__(self, w: int, h: int, vmin, vmax):
        self._w, self._h = w, h
        self._matrix = []
        self._errors = 0

        for i in range (w*h):
            r = randint(vmin, vmax)
            self._matrix.append(r)

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def message(self) -> str:
        return "Puzzle solved!"

    def value_at(self, x: int, y: int) -> str:
        m, w, h = self._matrix, self._w, self._h
        if 0 <= y < h and 0 <= x < w:
            if m[y * w + x] >-1:
                return str(m[y * w + x])
        return ""

    def play_at(self, x: int, y: int):
        if 0 <= y < self._h and 0 <= x < self._w:
            val = self._matrix[y*self.cols()+x]
            greatest = max(self._matrix)

            if val == greatest:
                self._matrix[y*self.cols()+x] = -1
            else:
                self._errors +=1

    def flag_at(self, x: int, y: int):
        pass

    def finished(self) -> bool:
        return self._board == [-1]*(self._h*self._w)

def main():
    game = Greatest(6,6, 10, 99)
    gui_play(game)
    ##console_play(game)

main()
