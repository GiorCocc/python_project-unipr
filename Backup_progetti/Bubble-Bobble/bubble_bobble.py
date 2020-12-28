from actor import Arena, Actor
from random import choice, randint
import random
import g2d_pyg as g2d

MIN_DIMENSION = 20

class Bonus(Actor):
    def __init__(self, arena, position):
        self._x, self._y = position
        self._w, self._h = 13, 11
        self._arena = arena
        arena.add(self)

    def move(self):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 278, 827, self._w, self._h

    def collide (self, other):
        if isinstance(other, Dragon):
            self._arena.remove(self)
            other.points()

class Platform(Actor):
    def __init__(self,arena,position, w, h):
        self._x, self._y = position
        self._w = MIN_DIMENSION * w
        self._h = MIN_DIMENSION * h
        self._arena = arena
        arena.add(self)

    def move(self):
        pass
        
    def fill(self):
        g2d.set_color((0,0,0))
        g2d.fill_rect((self._x, self._y, self._w, self._h))
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 0, 0, 0

    def collide(self, other):
        pass

class Enemy(Actor):                                     #condivide molto del codice del personaggio
    def __init__(self, position, arena):
        self._x, self._y = position
        self._w, self._h = 20, 20
        self._dx, self._dy = 0, 0
        self._gravity = 0.5
        self._speed = 3
        self._lives = 150
        self._arena = arena
        self._landed = False

        arena.add(self)

    def lives(self):
        return self._lives
        
    def move(self):        
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._landed = True

        self._x += self._dx
        if self._x < 0:
            self._x = 0
            self.decision(3)
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w
            self.decision(2)
        self._dy += self._gravity

    def decision(self, risp):
        if risp == 1:
            self.go_up()
        elif risp == 2 :
            self.go_left()
        elif risp == 3:
            self.go_right()

    def go_up(self):
        if self._landed:
            self._dy = -self._speed * 2
            self._landed = False
    
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed

    def collide(self, other):
        if isinstance(other, Platform) and self._dy >=0:
            x1, y1, w1, h1 = self.position()  # self's pos
            x2, y2, w2, h2 = other.position() # wall's pos
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0), (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
            
            move = min(borders)  # find nearest border: ←→↑↓
            distance, sign_dx, sign_dy = move
            self._x += sign_dx * distance
            self._y += sign_dy * distance

            if sign_dy < 0:
                self._landed = True
            if sign_dy != 0:
                self._dy = 1

        # per uccidere il nemico lo bombardo fino a quando esaurisce le sue vite. perde vite ad ogni istanza ma ha la possibilità di scappare
        if isinstance(other, Bubble):
            x2, y2, w2, h2 = other.position()
            self._x, self._y = x2, y2
            self._lives -=1
            if self._lives <= 0:
                self._arena.remove(self)

        if isinstance (other, Enemy):
            x2, y2, w2, h2 = other.position()
            x1, y1, w1, h1 = self.position()

            if abs(x1 - x2) < w1:
                self._dx = - self._dx


    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            return 5, 278, self._w, self._h
        elif self._dx > 0:
            return 1269, 278, self._w, self._h

class Dragon(Actor):
    def __init__(self, arena, position, platform):
        self._x, self._y = position
        self._w, self._h = 20, 20
        self._speed = 3
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._arena = arena
        self._gravity = 0.3
        self._platform = platform
        self._landed = False
        self._points = 0

        arena.add(self)

    def restore(self, position):
        self._x, self._y = position
        self._dx, self._dy = 0, 0
        self._landed = False

        self._arena.add(self)

    def points(self):
        self._points += 1
        return self._points

    def move(self):
        arena_w, arena_h = self._arena.size()
        self._y += self._dy
        if self._y < 0:
            self._y = 0
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._landed = True

        self._x += self._dx
        if self._x < 0:
            self._x = 0
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w
        self._dy += self._gravity

            
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed
        
    def go_up(self):
        if self._landed:
            self._dy = -self._speed * 2
            self._landed = False

    def stay(self):
        self._dx = 0

    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        if isinstance(other, Platform):
            x1, y1, w1, h1 = self.position()  # self's pos
            x2, y2, w2, h2 = other.position() # wall's pos
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0), (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
            
            move = min(borders)  # find nearest border: ←→↑↓
            distance, sign_dx, sign_dy = move
            self._x += sign_dx * distance
            self._y += sign_dy * distance

            if self._y >= y2 + h2:        #controllo se il personaggio si trova sotto alla piattaforma per farlo salire sopra
                self._y = y2

            if sign_dy < 0:
                self._landed = True
            if sign_dy != 0:
                self._dy = 1

        if isinstance(other, Enemy):
            self._lives -=1
            self.restore((40,40))
        
        if isinstance(other, Bubble):
            self._arena.remove(other)
        
    def position(self):
        return self._x, self._y, self._w, self._h


    def symbol(self):
        if self._dy < 0 and self._dx > 0:               #salto verso destra
            return 1037, 36, self._w, self._h
        elif self._dy < 0 and self._dx < 0:             #salto verso sinistra
            return 238, 36, self._w, self._h
        elif self._dx < 0 and self._dy > 0:             #sinistra
            return 6, 16, self._w, self._h
        elif self._dy < 0 and self._dx < 0:             #sinistra
            return 6, 16, self._w, self._h
        elif self._dx > 0 and self._dy > 0:             #destra
            return 1268, 16, self._w, self._h
        elif self._dx > 0 and self._dy < 0:             #destra
            return 1268, 16, self._w, self._h
        elif self._dy > 0 and self._dx < 0:             #caduta verso sinistra
            return 301, 36, self._w, self._h
        elif self._dy > 0 and self._dx < 0:             #caduta verso destra
            return 975, 36, self._w, self._h
        else:
            return 1268, 16, self._w, self._h

class Bubble(Actor):
    def __init__(self, arena, position, state):
        self._x, self._y = position
        self._ox, self._oy = position         #posizione di origine in cui viene creata la bolla
        self._w, self._h = 14, 16
        self._dx, self._dy = state, -3        #direzione di movimento, velocità di salita
        self._speed = 5
        self._arena = arena
        self._distance = 80
        arena.add(self)

    def update(self, x, y):
        self._x, self._y = x, y

    def move(self):
        arena_w, arena_h = self._arena.size()            

        self._x += self._dx
        if self._x < 0:
            self._x = 0
            self._arena.remove(self)
        elif self._x > arena_w - self._w:
            self._x = arena_w - self._w
            self._arena.remove(self)

        # controllo la distanza della bolla dalla sua origine per cambiarne la direzione
        if abs(self._x - self._ox) > self._distance:
            self._y += self._dy
            self._dx = 0

        if self._y < 0:
            self._y = 0
            self._arena.remove(self)
        elif self._y > arena_h - self._h:
            self._y = arena_h - self._h
            self._arena.remove(self)

    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed
        
    def go_up(self):
        self._dy = -self._speed

    def collide(self, other):
        pass

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 115, 1072, self._w, self._h
