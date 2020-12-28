from random import randint
m=10
continua="s"
while m>0 or continua!="n":
    
    n=randint(1,4)
    x=int(input("Quante monete vuoi puntare?"))
    while x>m:
        x=int(input("Quante monete vuoi puntare?"))
    s=int(input("Che numero scegli?"))
    while s<1 or s>4:
        s=int(input("Che numero scegli?"))
    if s==n:
        m=m+x
        print("Bravo! Hai Vinto!")
    else:
        m=m-x
        print("Peccato! Hai Perso!")
    print("Hai ancora", m, "monete")
    continua=input("Vuoi giocare ancora? [s/n]")


