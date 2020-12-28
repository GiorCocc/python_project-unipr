cols=5
rows=0
lista=[]
ripetuti=[]

    
def ripetizioni(lista):
    for i in range(len(lista)):
        for j in range (len(lista)-1):
            if lista[i]==lista[j]:
                x, y = i % cols, i // cols
                ripetuti.append((lista[i], x, y))

    for i in ripetuti:
        for j in ripetuti:
            if i==j:
                ripetuti.remove(j)
        

with open("matrice.csv", "r") as file:
    lines=file.readlines()
    rows=len(lines)
    for i in range (rows):
        x,y,z,k,j=lines[i].split(",")
        lista.append(int(x))
        lista.append(int(y))
        lista.append(int(z))
        lista.append(int(k))
        lista.append(int(j))
    ripetizioni(lista) 
    print(ripetuti)

