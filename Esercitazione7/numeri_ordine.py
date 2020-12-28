from boardgame import BoardGame
from boardgamegui import gui_play
from random import randint

class Matrice(BoardGame):
    def __init__(self, w, h, min, max):
        self._w, self._h = w, h
        self._min, self._max = min, max
        self._board = []
        self._error = 0

        for i in range (w*h):
            self._board.append(randint(self._min, self._max))
        
        print(self._board)

    def cols(self):
        return self._w

    def rows(self):
        return self._h

    def message(self):
        return "Hai risolto il puzzel ma hai commesso " + str(self._error) + " errori"

    def value_at(self, x, y):
        b, w, h = self._board, self._w, self._h
        if 0 <= y < h and 0 <= x < w and b[y * w + x] > 0:
            return str(b[y * w + x])
        return ""

    def massimo(self):
        massimo=0

        for el in self._board:
            if el >= massimo:
                massimo = el

        return massimo

    def play_at(self, x, y):
        b, w, h = self._board, self._w, self._h
        massimo = self.massimo()
        if 0 <= y < h and 0 <= x < w:
            if b[y * w + x]==massimo:
                b[y * w + x] = 0
            else:
                self._error+=1

    def flag_at(self, x, y):
        pass

    def finished(self):
        for el in self._board:
            if el!=0:
                return False
        return True
        

def main():
    game = Matrice(4,4,1,50)
    gui_play(game)
    #console_play(game)

main()

        