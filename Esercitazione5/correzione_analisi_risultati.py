counts=[0]*4
maxd=0

with open("passeggiata.txt", "r") as f:
    for line in f:
        r,x,y=[int(v) for v in line.split(",")]
        counts[r]+=1
        d=x**2+y**2
        if d>=maxd:
            maxd=d
    print(counts)
    print(maxd)        