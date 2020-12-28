from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import randint, choice

GRAY, WHITE, BLACK = 0, 1, 2


class Three(BoardGame):
    def __init__(self, w: int, h: int, locked: list):
        self._w, self._h = w, h
        self._board = [] * (w * h)
        self._lockedcells = locked
        self._nogray = False
        self._half = False
        self._contigue = False
        self._solvable = True

        for v in self._lockedcells:
            self._board.append(v)

    def cols(self):
        return self._w

    def rows(self):
        return self._h

    def message(self):
        return "Puzzle solved!"

    def value_at(self, x, y):
        b, w, h = self._board, self._w, self._h
        if 0 <= y < h and 0 <= x < w and b[y * w + x] > 0:
            if b[y * w + x] == WHITE:
                return "W"
            elif b[y * w + x] == BLACK:
                return "B"
        return ""

    def play_at(self, x, y):
        w, h, b, l = self._w, self._h, self._board, self._lockedcells
        if 0 <= y < h and 0 <= x < w:
            i = y * w + x
            if l[i] == GRAY:
                if b[i] == GRAY:  # grigio
                    b[i] = WHITE
                elif b[i] == WHITE:  # bianco
                    b[i] = BLACK
                elif b[i] == BLACK:  # nero
                    b[i] = GRAY

    def flag_at(self, x, y):
        pass

    def nogray(self):
        for el in self._board:
            if el == GRAY:
                self._nogray = False
                return self._nogray

        self._nogray = True
        return self._nogray

    def halfcolor(self):
        for y in range(self.rows()):
            cont_w, cont_b, cont_g = 0, 0, 0
            for x in range(self.cols()):
                index = y * self.cols() + x
                if self._board[index] == WHITE:
                    cont_w += 1
                elif self._board[index] == BLACK:
                    cont_b += 1
                else:
                    cont_g += 1

            if cont_b != cont_w and cont_g == GRAY:
                self._half = False
                return self._half
            elif cont_b == cont_w and cont_g != GRAY:
                return
            elif cont_b != cont_w and cont_g != GRAY:
                return

        for x in range(self.rows()):
            cont_w, cont_b, cont_g = 0, 0, 0
            for y in range(self.cols()):
                index = y * self.cols() + x
                if self._board[index] == WHITE:
                    cont_w += 1
                elif self._board[index] == BLACK:
                    cont_b += 1
                else:
                    cont_g += 1

            if cont_b != cont_w and cont_g == GRAY:
                self._half = False
                return self._half
            elif cont_b == cont_w and cont_g != GRAY:
                return
            elif cont_b != cont_w and cont_g != GRAY:
                return

        self._half = True
        return self._half

    def contigue(self):
        matrix = []
        for y in range(self.rows()):
            new_row = []
            for x in range(self.cols()):
                index = y * self.cols() + x
                new_row.append(self._board[index])
            matrix.append(new_row)

        cont = 0
        for x in range(self.rows()):
            for y in range(self.cols()):
                if matrix[x][y] != GRAY:
                    if 0 <= x-1 < self.rows():
                        if matrix[x-1][y] != GRAY:
                            if matrix[x][y] == matrix[x-1][y]:
                                if 0 <= x-2 < self.rows():
                                    if matrix[x-2][y] != GRAY:
                                        if matrix[x][y] == matrix[x-2][y]:
                                            # print(1)
                                            # print(x,y)
                                            return self._contigue

                    if 0 <= x+1 < self.rows():
                        if matrix[x+1][y] != GRAY:
                            if matrix[x][y] == matrix[x+1][y]:
                                if 0 <= x+2 < self.rows():
                                    if matrix[x+2][y] != GRAY:
                                        if matrix[x][y] == matrix[x+2][y]:
                                            # print(2)
                                            # print(x,y)
                                            return self._contigue

                    if 0 <= y-1 < self.cols():
                        if matrix[x][y-1] != GRAY:
                            if matrix[x][y] == matrix[x][y-1]:
                                if 0 <= y-2 < self.cols():
                                    if matrix[x][y-2] != GRAY:
                                        if matrix[x][y] == matrix[x][y-2]:
                                            # print(3)
                                            # print(x,y)
                                            return self._contigue

                    if 0 <= y+1 < self.cols():
                        if matrix[x][y+1] != GRAY:
                            if matrix[x][y] == matrix[x][y+1]:
                                if 0 <= y+2 < self.cols():
                                    if matrix[x][y+2] != GRAY:
                                        if matrix[x][y] == matrix[x][y+2]:
                                            # print(4)
                                            # print(x,y)
                                            return self._contigue
                else:
                    cont += 1
                    # print(cont)

        if cont == 0:
            self._contigue = True
            return self._contigue
        else:
            return

    def auto_line(self):
        trovato = False
        # controllo che il numero delle celle bianche e nere sulle righe
        y = 0
        while y < self.rows() and trovato == False:
            white, black, gray = 0, 0, 0
            for x in range(self.cols()):
                index = y*self.cols()+x
                # conto separatamente le celle bianche quelle nere e quelle grige
                if self._board[index] == WHITE:
                    white += 1
                elif self._board[index] == BLACK:
                    black += 1
                else:
                    gray += 1
            # per poter riempire automaticamente la riga, devo avere alemneno una cella vuota
            if (white == self.cols()/2 or black == self.cols()/2) and gray > 0:
                trovato = True
            else:
                y += 1

        # codice per il riempimento della cella vuota con il colore corretto
        if trovato == True:
            if white == self.cols()/2:
                for x in range(self.cols()):
                    index = y*self.cols()+x
                    if self._board[index] == GRAY:
                        self._board[index] = BLACK
            elif black == self.cols()/2:
                for x in range(self.cols()):
                    index = y*self.cols()+x
                    if self._board[index] == GRAY:
                        self._board[index] = WHITE
            return  # inserisco return per poter eseguire un riempimento solo alla volta

        # stesso codice per le righe eseguito sulle colonne
        if trovato == False:
            x = 0
            while x < self.cols() and trovato == False:
                white, black, gray = 0, 0, 0
                for y in range(self.rows()):
                    index = y*self.cols()+x
                    if self._board[index] == WHITE:
                        white += 1
                    elif self._board[index] == BLACK:
                        black += 1
                    else:
                        gray += 1
                if (white == self.cols()/2 or black == self.cols()/2) and gray > 0:
                    trovato = True
                else:
                    x += 1

        if trovato == True:
            if white == self.cols()/2:
                for y in range(self.cols()):
                    index = y*self.cols()+x
                    if self._board[index] == GRAY:
                        self._board[index] = BLACK
            elif black == self.cols()/2:
                for y in range(self.cols()):
                    index = y*self.cols()+x
                    if self._board[index] == GRAY:
                        self._board[index] = WHITE
            return

    def auto_terna(self):
        # controllo se ci sono due celle uguali sulle righe
        for y in range(self.rows()):
            # diminuisco il range della x in modo da comprire comunque con gli indici tutti i valori senza effettuare controlli
            for x in range(self.cols()-2):
                index0 = y*self.cols()+x
                index1 = index0+1
                index2 = index0+2
                # controllo le 2 celle adiacenti e la terza vuota
                if self._board[index0] == self._board[index1] and self._board[index2] == GRAY:
                    if self._board[index0] == WHITE:
                        self._board[index2] = BLACK
                        return          # inserisco il return per eseguire solo un riempimento alla volta e non tutti insieme
                    elif self._board[index0] == BLACK:
                        self._board[index2] = WHITE
                        return
                # eseguo lo stesso controllo anche nel senso opposto
                if self._board[index2] == self._board[index1] and self._board[index0] == GRAY:
                    if self._board[index2] == WHITE:
                        self._board[index0] = BLACK
                        return
                    elif self._board[index2] == 2:
                        self._board[index0] = WHITE
                        return

        # eseguo gli stessi controlli fatti per le righe anche per le colonne
        for x in range(self.cols()):
            for y in range(self.rows()-2):
                index0 = y*self.cols()+x
                index1 = (y+1)*self.cols()+x
                index2 = (y+2)*self.cols()+x
                if self._board[index0] == self._board[index1] and self._board[index2] == GRAY:
                    if self._board[index0] == WHITE:
                        self._board[index2] = BLACK
                        return
                    elif self._board[index0] == BLACK:
                        self._board[index2] = WHITE
                        return
                if self._board[index2] == self._board[index1] and self._board[index0] == GRAY:
                    if self._board[index2] == WHITE:
                        self._board[index0] = BLACK
                        return
                    elif self._board[index2] == BLACK:
                        self._board[index0] = WHITE
                        return

    def unsolvable(self):
        if self.halfcolor() == None and self.contigue() == None:
            return False
        elif self.halfcolor() == False or self.contigue() == False:
            return True

    def solve(self, i: int):
        self.auto_line()
        self.auto_terna()
        if self.unsolvable():
            return False

        while i < len(self._board) and self._board[i] != GRAY:
            i += 1
        if i < len(self._board):
            saved = self._board[:]
            for color in (BLACK, WHITE):
                self._board[i] = color
                if self.solve(i + 1):
                    return True
                self._board = saved
        return self.finished()

    def finished(self):
        return self.nogray() and self.halfcolor() and self.contigue()


def lockedcells(locked, e: int):
    config = []
    possibilities = []
    with open("config.txt") as f:
        for line in f:
            v = line.split(",")
            new_line = []
            for n in v:
                x = n
                new_line.append(x)
            config.append(new_line)

    for lista in config:
        if len(lista) == e*e:
            possibilities.append(lista)

    index = randint(0, len(possibilities)-1)

    for val in possibilities[index]:
        locked.append(int(val))

    return locked


def main():
    locked = []
    n = int(input("Dimensione matrice (6,8,10,12,14)?"))
    lockedcells(locked, n)
    game = Three(n, n, locked)
    gui_play(game)
    # console_play(game)


main()
