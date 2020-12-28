text = input("text? ")

for c in text:
    if c in "aeiou": #controlla se un elemento fa parte di una sequenza
        print(c.upper(), end="") #end="" serve per mettere le lettere una in fila all'altra
    else:
        print(c, end="")