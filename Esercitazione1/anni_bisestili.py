anno=int(input("Inserisci un anno:"))
while anno!=0:
    
    bis=anno%4
    if bis==0:
        print("L'anno è bisestile")
    else:
        print("L'anno non è bisestile")
    anno=int(input("Inserisci un anno:"))
