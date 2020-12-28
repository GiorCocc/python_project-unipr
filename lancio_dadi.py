from random import randint

n=int(input("n?"))

count=[0]*13

for i in range(n):
    die1=randint(1,6)
    die2=randint(1,6)
    val=die1+die2
    count[val]+=1

    
