from Actor import Arena, Actor
from random import choice, randint
import random
import  g2d

sprites = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")

class Platform(Actor):
    def __init__(self,arena,position):
        self._x, self._y = position
        self._w = 150
        self._h = 10
        self._arena = arena
        arena.add(self)
        
    def move(self):
        g2d.set_color((0,0,0))
        g2d.fill_rect((self._x,self._y,self._w,self._h))
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0, 0, 0, 0

    def collide(self, other):
        pass

class Enemy(Actor):
    def __init__(self, position, arena):
        self._x, self._y=position
        self._w, self._h = 20, 20
        self._dx, self._dy=randint(2,5),randint(2,5)
        self._gravity=0.5
        self._speed=4
        self._arena=arena
        self._landed=False
        self._lives=1

        arena.add(self)
        
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

    def decision(self):
        risp = randint(1,5)
        if risp == 5:
            self.go_up()
        elif risp == 1 or risp == 2 :
            self.go_left()
        elif risp == 3 or risp == 4 :
            self.go_right()
    def go_up(self):
        if self._landed:
            self._dy = -self._speed*2
            self._landed = False
    
    def go_left(self):
        self._dx = -self._speed

    def go_right(self):
        self._dx = self._speed

    def collide(self, other):
        #fare i modo che cambi direzione quando collide con la parete (vedi ball)
        if isinstance(other, Platform):
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

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        return 5,278, self._w, self._h

class Dragon(Actor):
    def __init__(self, arena, position, platform):
        self._x, self._y = position
        self._w, self._h = 20, 20
        self._speed = 4
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._arena = arena
        self._gravity = 0.3
        self._landed = False

        arena.add(self)

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
            self._dy = -self._speed*2
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

            if self._y >= y2+h2:
                self._y = y2-h2

            if sign_dy < 0:
                self._landed = True
            if sign_dy != 0:
                self._dy = 1
            
        if isinstance(other, Enemy):
            self._lives = 0

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
    def live(self):
        return self._lives

arena = Arena((480, 360))
platform = [Platform(arena, (80,320)), Platform(arena, (300,320)), Platform(arena, (80,200))]
enemy = Enemy((80,30), arena)
dragon = Dragon(arena, (40, 40), platform)


def tick():
    if g2d.key_pressed("ArrowUp"):
        dragon.go_up()
    elif g2d.key_pressed("ArrowRight"):
        dragon.go_right()
    elif g2d.key_pressed("ArrowLeft"):
        dragon.go_left()
    elif (g2d.key_released("ArrowLeft") or g2d.key_released("ArrowRight")):
        dragon.stay()
    enemy.decision()

    if dragon.live() == 0:
        arena.remove(dragon)
    arena.move_all()  # Game logic
    
    g2d.clear_canvas()
    for i in platform: 
        i.move()
    for a in arena.actors():
        if a.symbol() != (0, 0, 0, 0):
            g2d.draw_image_clip(sprites, a.symbol(), a.position())
        else:
            g2d.fill_rect(a.position())
    
def main():
    
    g2d.init_canvas(arena.size())
    g2d.main_loop(tick)

main()