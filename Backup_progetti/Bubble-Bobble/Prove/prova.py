from random import randint

with open("prova.txt", "w") as p:
    for i in range (30):
        print(randint(0,30), file=p)