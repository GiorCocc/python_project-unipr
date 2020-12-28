n=int(input("Dimmi un numero:"))
for count in range(1,n+1):
    d=n%count
    if d==0:
        print(count)
