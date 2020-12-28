from actor import Arena, Actor
from random import choice, randint
import random
import g2d_pyg as g2d

# variabili globali
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
            self._arena.remove(self)    # rimozione della bolla a contatto con il drago

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
        g2d.set_color((99, 92, 92))
        g2d.fill_rect((self._x, self._y, self._w, self._h))
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 0, 0, 0

    def collide(self, other):
        pass

class Enemy(Actor):                                     
    def __init__(self, position, arena):
        self._x, self._y = position
        self._w, self._h = 15, 16
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

    def decision(self, risp):   #metodo per l'assegnazione della direzione di movimento per il nemico
        if risp == 1:
            self.go_up()
        elif risp == 2 :
            self.go_left()
        elif risp == 3:
            self.go_right()

    def go_up(self):
        if self._landed:
            self._dy = -self._speed * 2.5
            self._landed = False
    
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed

    def collide(self, other):
        if isinstance(other, Platform) and self._dy >=0:
            x1, y1, w1, h1 = self.position()
            x2, y2, w2, h2 = other.position()
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0), (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
            
            move = min(borders)
            distance, sign_dx, sign_dy = move
            self._x += sign_dx * distance
            self._y += sign_dy * distance

            if sign_dy < 0:
                self._landed = True
            if sign_dy != 0:
                self._dy = 1

        # per sconfiggere il nemico lo colpisco con le bolle; la bolla lo intrappola ma il nemico può scappare
        if isinstance(other, Bubble):
            x2, y2, w2, h2 = other.position()
            self._x, self._y = x2, y2
            self._lives -=1
            if self._lives <= 0:
                self._arena.remove(self)

        # due nemici che entrano in contatto cambiano le rispettive direzioni di movimento
        if isinstance (other, Enemy):
            x2, y2, w2, h2 = other.position()
            x1, y1, w1, h1 = self.position()

            if abs(x1 - x2) < w1:
                self._dx = - self._dx


    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dx < 0:
            return 6, 455, self._w, self._h
        elif self._dx > 0:
            return 1269, 455, self._w, self._h

class Dragon(Actor):
    def __init__(self, arena, position):
        self._x, self._y = position
        self._x0 , self._y0 = position          # posizione di origine per permetterne il ripristino
        self._w, self._h = 20, 20
        self._speed = 3
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._arena = arena
        self._gravity = 0.3
        self._landed = False
        self._points = 0

        arena.add(self)

    def restore(self):
        self._x, self._y = self._x0 , self._y0
        self._dx, self._dy = 0, 0
        self._landed = False

        self._arena.add(self)

    def points(self):
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
        if isinstance(other, Platform) and self._dy >=0:
            x1, y1, w1, h1 = self.position()
            x2, y2, w2, h2 = other.position()
            borders = [(x1+w1 - x2, -1, 0), (x2+w2 - x1, 1, 0), (y1+h1 - y2, 0, -1), (y2+h2 - y1, 0, 1)]
            
            move = min(borders)
            distance, sign_dx, sign_dy = move
            self._x += sign_dx * distance
            self._y += sign_dy * distance

            if sign_dy < 0:
                self._landed = True
            if sign_dy != 0:
                self._dy = 1

        # alla collisione con un nemico, il drago per una vita
        if isinstance(other, Enemy):
            self._lives -=1
            self.restore()
        
        # alla collisione con una bolla, la bolla viene fatta esplodere
        if isinstance(other, Bubble):
            self._arena.remove(other)

        # alla collisione con un bonus, i punti si aggiornano
        if isinstance(other, Bonus):
            self._points += 5
        
    def position(self):
        return self._x, self._y, self._w, self._h


    def symbol(self):
        if self._dy < 0 and self._dx > 0:               # salto verso destra
            return 1037, 36, self._w, self._h
        elif self._dy < 0 and self._dx < 0:             # salto verso sinistra
            return 238, 36, self._w, self._h
        elif self._dx < 0 and self._dy > 0:             # sinistra
            return 6, 16, self._w, self._h
        elif self._dy < 0 and self._dx < 0:             # sinistra
            return 6, 16, self._w, self._h
        elif self._dx > 0 and self._dy > 0:             # destra
            return 1268, 16, self._w, self._h
        elif self._dx > 0 and self._dy < 0:             # destra
            return 1268, 16, self._w, self._h
        else:
            return 1267, 189, self._w, self._h

class Bubble(Actor):
    def __init__(self, arena, position, state):
        self._x, self._y = position
        self._ox, self._oy = position         # posizione di origine in cui viene creata la bolla
        self._w, self._h = 14, 16
        self._dx, self._dy = state, -3        # direzione di movimento, velocità di salita
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

        # rimuovo la bolla quando urta i bordi laterali
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
