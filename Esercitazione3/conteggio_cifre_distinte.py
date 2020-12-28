def conta_zero(s):
    ris=[0]*10
    for z in range (0,10):
        count=0
        for i in s:
            if i==str(z):
                count+=1
        ris[z]=count
    stampa_lista(ris)

def stampa_lista(lista):
    for i in range (0,10):
        print("Ci sono", lista[i], "cifre uguali a", i)

def main():
    string=str(input("Dammi una serie di valori:"))
    conta_zero(string)


main()