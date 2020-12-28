points=[]

max_d=0
max_p=(0,0)
max_q=(0,0)

with open ("passeggiata.txt") as f:
    for line in f:
        r, x, y = [int(v) for v in line.split(",")]

        point = x, y
        points.append(point)

for p_index in range (len(points)):
    p = points[p_index]
    for q_index in range (p_index + 1, len(points)):
        q=points[q_index]
        x1,y1=p
        x2,y2=q
        d=((abs(x1-x2))**2 + (abs(x1-x2))**2)**0.5
        if max_d<d:
            max_d=d
            max_p=p
            max_q=q

print(max_d, max_p, max_q)