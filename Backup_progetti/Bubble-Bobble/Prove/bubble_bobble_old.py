from actor import Arena, Actor
import g2d

sprites = g2d.load_image("https://tomamic.github.io/images/sprites/bubble-bobble.png")

class Rect(Actor):
    def __init__(self,arena,pos):
        self._arena_w, self._arena_h = arena.size()
        self._x, self._y = pos
        self._w = 150
        self._h = 20
        arena.add(self)
        
    def move(self):
        g2d.set_color((0,0,0))
        g2d.fill_rect((self._x,self._y,self._w,self._h))
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol (self):
        return 0,0,0,0

    def collide(self, other):
        pass

class Dragon(Actor):
    def __init__(self, arena, pos,r1):
        
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._speed = 3
        self._dx, self._dy = 0, 0
        self._lives = 3
        self._last_collision = 0
        self._arena = arena
        self._gravity = 0.3
        self._rect=r1
        self._landed=False
        arena.add(self)

    def move(self):
        arena_w, arena_h = self._arena.size()

        if (self._y == arena_h - self._h):
            self._landed=True

        for i in r1:
            xr,yr,wr,hr = i.position()
            self._y += self._dy
            self._x += self._dx

            if self._y <= yr and self._y >= yr-hr  and self._x >= xr and self._x <= xr+wr:
                self._x = self._x
                self._y = yr-hr
                self._dy = 0
                self._landed=True
                
            elif self._x > arena_w - self._w:
                self._x = arena_w - self._w
            elif self._y > arena_h - self._h:
                self._y = arena_h - self._h
            else:
                self._dy+=self._gravity

            
    def go_left(self, go: bool):
        if go:
            self._dx = -self._speed
        elif self._dx < 0:
            self._dx = 0

    def go_right(self, go: bool):
        if go:
            self._dx = self._speed
        elif self._dx > 0:
            self._dx = 0

    def go_up(self):
        if self._landed:
            self._dy = -self._speed*2
            self._landed=False
        elif self._dy < 0:
            self._dy = 0

    def go_down(self, go: bool):
        if go:
            self._dy = self._speed
        elif self._dy > 0:
            self._dy = 0

    def lives(self) -> int:
        return self._lives

    def collide(self, other):
        if self._arena.count() - self._last_collision < 30:
            return
        self._last_collision = self._arena.count()

    def position(self):
        return self._x, self._y, self._w, self._h

    def symbol(self):
        if self._dy<0 and self._dx>0:               #salto verso destra
            return 1037,36, self._w, self._h
        elif self._dy<0 and self._dx<0:             #salto verso sinistra
            return 238,36, self._w, self._h
        elif self._dx<0 and self._dy>0:             #sinistra
            return 6,16, self._w, self._h
        elif self._dy<0 and self._dx<0:             #sinistra
            return 6,16, self._w, self._h
        elif self._dx>0 and self._dy>0:             #destra
            return 1268, 16, self._w, self._h
        elif self._dx>0 and self._dy<0:             #destra
            return 1268, 16, self._w, self._h
        elif self._dy>0 and self._dx<0:             #caduta verso sinistra
            return 301,36, self._w, self._h
        elif self._dy>0 and self._dx<0:             #caduta verso destra
            return 975, 36, self._w, self._h
        else:
            return 1268, 16, self._w, self._h


arena = Arena((480, 360))
r1 = [Rect(arena, (80,320)),Rect(arena, (300,320)),Rect(arena, (80,200))]
# r1=Rect(arena, (80,200))
dragon = Dragon(arena, (40, 40), r1)

def tick():
    if g2d.key_pressed("ArrowUp"):
        dragon.go_up()
    if g2d.key_pressed("ArrowRight"):
        dragon.go_right(True)
    elif g2d.key_released("ArrowRight"):
        dragon.go_right(False)
    if g2d.key_pressed("ArrowDown"):
        dragon.go_down(True)
    elif g2d.key_released("ArrowDown"):
        dragon.go_down(False)
    if g2d.key_pressed("ArrowLeft"):
        dragon.go_left(True)
    elif g2d.key_released("ArrowLeft"):
        dragon.go_left(False)

    arena.move_all()  # Game logic
    
    g2d.clear_canvas()
    for i in r1: 
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