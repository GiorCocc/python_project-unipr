anno=int(input("Inserisci un anno:"))

#usando la tabella booleana
if anno%400==0 or anno%100!=0 and anno%4==0:
    print("L'anno è bisestile")
else:
    print("L'anno non è bisestile")
