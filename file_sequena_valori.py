import random

n=random.randint(0,100)
max_val=None

with open("random.txt", "w") as f:
    for i in range(n):
        r=random.random()
        print(r)

with open("random.txt", "r") as f:
    for line in f:
        val=float(line)
        if max_val is None or val>max_val:
            max_val=val
            
    print(max_val)