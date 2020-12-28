#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d
from pallina_con_gravita import FallingBall, ARENA_W, ARENA_H

b1 = FallingBall(40, 80)


def tick():
    g2d.clear_canvas()  # BG
    b1.move()
    g2d.fill_rect(b1.position())  # FG

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)

main()
