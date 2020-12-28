from math import sqrt

direction=[0]*4
list_x=[]
list_y=[]
x_tot=0
y_tot=0

with open('passeggiata.txt', 'r') as passeggiata:
    line=passeggiata.readlines()
    for i in range (len(line)):
        r,x,y=line[i].split(",",-1)
        list_x.append(int(x))
        list_y.append(int(y))
        
        if r=="0 ":
            direction[0]+=1
        elif r=="1 ":
            direction[1]+=1
        elif r=="2 ":
            direction[2]+=1
        elif r=="3 ":
            direction[3]+=1

    for el in list_x:
        x_tot+=el

    for el in list_y:
        y_tot+=el
        
    d=sqrt((x_tot+ list_x[0])**2 + (y_tot + list_y[0])**2)

print("Sei andato su", direction[0], "volte, a destra", direction[1], "volte, in basso", direction[2], "volte e a sinistra", direction[3], "volte")
print(f"La distanza tra il primo e l'ultimo punto è: {d: 4.2f}" )
