#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from pallina_con_controlli_correzione import HeroBall, ARENA_W, ARENA_H

b1 = HeroBall(40, 80)


def tick():
    g2d.clear_canvas()  # BG

    if g2d.key_pressed("w"):
        b1.go_up()
    if g2d.key_pressed("a"):
        b1.go_left()
    if g2d.key_pressed("s"):
        b1.go_down()
    if g2d.key_pressed("d"):
        b1.go_right()

    b1.move()
    g2d.fill_rect(b1.position())  # FG

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()