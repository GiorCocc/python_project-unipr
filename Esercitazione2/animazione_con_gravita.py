import g2d

x, y, dx, dy = 50, 50, 5,5
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20
image = g2d.load_image("ball.png")
g=0.4

def tick():
    global x,y, dx, dy
    if x + dx < 0 or x + dx + BALL_W > ARENA_W:
        dx = -dx
    if y + dy < 0 or y + dy + BALL_H > ARENA_H:
        dy = -dy
    g2d.clear_canvas()           
    g2d.draw_image(image, (x, y)) 
    x += dx                        
    dy+=g
    y+=dy

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  

main()

