from re import I


n=int(input("enter term : "))
i=1
p=n
while n!=0:
    if i%2!=0:
        c=i
        n-=1
    i+=1
print("first ",p," natural reverse odd number are :",end=' ')
while c>0:
    print(c,end=' ' )
    c-=2
    