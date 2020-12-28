import g2d #g2d_pygame

# way too much global stuff!
x1, y1, dx1, dy1 = 40, 180, 5, 5
x2, y2, dx2, dy2 = 180, 140, 5, 5
ARENA_W, ARENA_H, BALL_W, BALL_H = 480, 360, 20, 20
image = g2d.load_image("ball.png")

#controllo il codice che posso implementare per il grago

# encapsulates behaviour, but exposes data
def move_ball(x: int, y: int,
              dx: int, dy: int) -> (int, int, int, int):

    g=0.5
    if x + dx < 0 or x + dx + BALL_W > ARENA_W:
        dx = -dx
    x += dx
    if y + dy < 0 or y + dy + BALL_H > ARENA_H:
        dy = -dy
    else:
        dy+=g
    
    y += dy
    return x, y, dx, dy

def tick():
    global x1, y1, dx1, dy1
    global x2, y2, dx2, dy2
    g2d.clear_canvas()               # Draw background
    g2d.draw_image(image, (x1, y1))  # Draw foreground
    g2d.draw_image(image, (x2, y2))  # Draw foreground
    x1, y1, dx1, dy1 = move_ball(x1, y1, dx1, dy1)
    x2, y2, dx2, dy2 = move_ball(x2, y2, dx2, dy2)

def main():
    g2d.init_canvas((ARENA_W, ARENA_H))
    g2d.main_loop(tick)  # call tick 30 times/second

main()