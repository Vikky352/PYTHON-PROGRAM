l=int(input("Enter number of term: "))
c=2
s=set()
i=0
while i<l:
    count=0
    for j in range(2,c+1//2):
        if c%j==0: 
            count+=1
    if count==0:
        s.add(c)
        i+=1
    c+=1
print("First set of  %d natural numbers:"%l,s)


# it is good practice using for prime number
# import math as m
# int(m.sqrt(c))+1