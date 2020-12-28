from random import randint

rows=int(input("Quante righe"))
cols=int(input("Quante colonne"))
minimo=int(input("Soglia minima"))
massimo=int(input("Soglia massima"))
numeri_generati=[]

matrix = []
def controllo(n: int) ->bool:
    if len(numeri_generati)==0:
        return True

    for i in numeri_generati:
        if n==i:
            n=randint(minimo, massimo+1)
            controllo(n)
        else:
            numeri_generati.append(n)
            return True


for y in range(rows):
    new_row = []
    for x in range(cols):
        n=randint(minimo, massimo+1)
        if controllo(n):
            new_row.append(n)
    matrix.append(new_row)

with open("matrice_senza_ripetizioni.csv", "w") as file:
    for y in range(rows):
        for x in range (cols):
            v=matrix[y][x]
            sep="," if x<cols-1 else ""
            print(v, end=sep, file=file)
        print(file=file)

