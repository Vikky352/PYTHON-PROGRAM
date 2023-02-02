n=int(input("enter term : "))
i=1
c=0
p=n
for j in (1,n+1,0):
    # print(j)
    if i%2==0:
        c=c+i
        print(c,end=' ' )
        j+=1
    i=i+1
print("first ",p," natural reverse even number are :",end=' ')
#while c>0:
print(c,end=' ' )
   # c-=2
    