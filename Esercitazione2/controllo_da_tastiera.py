import g2d

x, y, dx, dy = 240, 240, 5,5
s=4
ARENA_W, ARENA_H = 480, 360
image = g2d.load_image("ball.png")

def tick():
    global x,y, dy, dx, s        

    g2d.clear_canvas()             # Draw background
    g2d.draw_image(image, (x, y))  # Draw foreground
    

    if g2d.key_pressed("w"):
        s=1
        # y-=dy
    elif g2d.key_pressed("a"):
        s=2
        # x-=dx
    elif g2d.key_pressed("s"):
        s=3
        # y+=dy
    elif g2d.key_pressed("d"):
        s=4
        # x+=dx
    
    if s==1:
        y-=dy
    elif s==2:
        x-=dx
    elif s==3:
        y+=dy
    elif s==4:
        x+=dx
    

    

    

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()
