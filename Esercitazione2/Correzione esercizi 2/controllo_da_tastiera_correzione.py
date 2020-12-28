import g2d

x, y, dx, dy = 50, 50, 0,0
ARENA_W, ARENA_H = 480, 360
image = g2d.load_image("ball.png")

def tick():
    global x,y,dy, dx
    if g2d.key_pressed("w"):
        dx=0
        dy=-5
    elif g2d.key_pressed("a"):
        dy=0
        dx=-5
    elif g2d.key_pressed("s"):
        dx=0
        dy=5
    elif g2d.key_pressed("d"):
        dy=0
        dx=5

    g2d.clear_canvas()             # Draw background
    g2d.draw_image(image, (x, y))  # Draw foreground
    
    x += dx                        # Update ball's position
    y += dy

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()