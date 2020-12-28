cols=4
lista=[]

val=int(input("quale valore? "))

with open("valori.csv", "r") as valori:
    line=valori.readlines()
    rows=len(line)
    for i in range (rows):
        x,y,z,k=line[i].split(",",-1)
        lista.append(int(x))
        lista.append(int(y))
        lista.append(int(z))
        lista.append(int(k))

    for j in range(len(lista)):
        if lista[j]==val:
            print("Le coordinate del punto ", val, "sono (", (j//cols)+1, ",", (j%cols)+1, ")")

