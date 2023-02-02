n=int(input("enter number of term:-"))

print("first %d prime numbers are:-"%n)
i=2
p=1
while n!=0:
    
        c=0
        
        for j in range(2,i-1):
         if i%j==0:
            c=c+1
        if c==0:
            print(i)
            n-=1
        i=i+1