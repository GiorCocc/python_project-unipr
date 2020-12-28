'''
Problemi da correggere
'''
from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import randint, choice

class Three(BoardGame):
    def __init__(self, w:int, h:int):
        self._w, self._h = w,h
        self._board = [] * (w * h)
        self._lockedcells = []
        self._nogray = False
        self._half = False
        self._contigue = False

        for v in self.lockedcells():
            self._board.append(v)


    def lockedcells(self):
        config = []
        possible_choice = []
        with open("config.txt") as f:
            for line in f:
                v = line.split(",")
                new_line = []
                for n in v:
                    x = int(n)
                    new_line.append(x)
                config.append(new_line)
        
        for v in config:
            if len(v) == self._w * self._h:
                possible_choice.append(v)

        index = randint(0, len(possible_choice)-1)

        for val in possible_choice[index]:
            self._lockedcells.append(val)

        return self._lockedcells


    def cols(self):
        return self._w

    def rows(self):
        return self._h

    def message(self):
        return "Puzzle solved!"

    def value_at(self, x, y):
        b, w, h = self._board, self._w, self._h
        if 0 <= y < h and 0 <= x < w and b[y * w + x] > 0:
            if b[y * w + x] == 1:
                return "W"
            elif b[y * w + x] == 2:
                return "B"
        return ""

    def play_at(self, x, y):
        w, h, b, l = self._w, self._h, self._board, self._lockedcells
        if 0 <= y < h and 0 <= x < w:
            i = y * w + x
            if l[i] == 0:
                if b[i] == 0:     #grigio
                    b[i] = 1
                elif b[i] == 1:   #bianco
                    b[i] = 2
                elif b[i] == 2:   #nero
                    b[i] = 0

    def flag_at(self, x, y):
        pass

    def nogray(self):
        for el in self._board:
            # controllo che non ci siano celle grige
            if el == 0:
                self._nogray=False
                return self._nogray

        self._nogray = True
        return self._nogray

    def halfcolor(self):
        count_w, count_b = 0,0
        for el in self._board:
            if el == 1:
                count_w+=1
            elif el == 2:
                count_b+=1

        if count_w == count_b:
            self._half=True
            return self._half
        else:
            self._half=False
            return self._half

    def contigue(self):
        matrix = []
        for y in range(self.rows()):
            new_row = []
            for x in range(self.cols()):
                index = y * self.cols() + x
                new_row.append(self._board[index])
            matrix.append(new_row)

        for x in range (self.rows()):
            for y in range (self.cols()):

                if 0 <= x-1 < self.rows():
                    if matrix[x][y] == matrix[x-1][y]:
                        if 0 <= x-2 < self.rows():
                            if matrix[x][y] == matrix[x-2][y]:
                                return self._contigue

                if 0 <= x+1 < self.rows():
                    if matrix[x][y] == matrix[x+1][y]:
                        if 0 <= x+2 < self.rows():
                            if matrix[x][y] == matrix[x+2][y]:
                                return self._contigue

                if 0 <= y-1 < self.cols():
                    if matrix[x][y] == matrix[x][y-1]:
                        if 0 <= y-2 < self.cols():
                            if matrix[x][y] == matrix[x][y-2]:
                                return self._contigue

                if 0 <= y+1 < self.cols():
                    if matrix[x][y] == matrix[x][y+1]:
                        if 0 <= y+2 < self.cols():
                            if matrix[x][y] == matrix[x][y+2]:
                                return self._contigue
        
        self._contigue = True
        return self._contigue


    def finished(self):
        return self.nogray() and self.halfcolor() and self.contigue()
        

def main():
    n=int(input("Dimensione matrice (6,8,10,12,14)?"))
    game = Three(n,n)
    gui_play(game)
    #console_play(game)

main()