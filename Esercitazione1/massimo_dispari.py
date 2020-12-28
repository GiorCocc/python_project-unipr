m=0
n=int(input("Dammi un valore [0 per terminare]:"))
while n>0:
    if n%2!=0:
        if m<n:
            m=n
    n=int(input("Dammi un valore [0 per terminare]:"))
print("il numero dispari più grande inserito è:", m)
