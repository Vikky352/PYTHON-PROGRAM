n=int(input("enter number: "))
print("prime factor of ",n,"are : ",end=' ')
for i in range(2,n//2):
    if n%i==0:
        c=0
        for j in range(2,i//2+1):
           if i%j==0:
               c+=1
        if c==0:
             print(i,end=' ')