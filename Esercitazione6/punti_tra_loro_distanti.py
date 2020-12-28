from math import sqrt

direction=[0]*4
lista=[]

distanza_massima=0
punti_massimo=0,0,0,0

with open('passeggiata.txt', 'r') as passeggiata:
    line=passeggiata.readlines()
    for i in range (len(line)):
        r,x,y=line[i].split(",",-1)
        lista.append((int(x), int(y)))

    for i in range(len(lista)):
        x,y=lista[i]
        for j in range (len(lista)):
            x1,y1=lista[j]

            d=sqrt((x1- x)**2 + (y1 - y)**2)
            #print(d)

            if d>=distanza_massima:
                distanza_massima=d
                punti_massimo=x1,y1,x,y

        
print(f"La distanza tra i punti più lontani({punti_massimo}) è: {distanza_massima: 4.2f}" )

