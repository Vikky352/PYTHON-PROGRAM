n=int(input("enter first number: "))
m=int(input("enter second number: "))
p=n
q=m
while n!=m:
    if n>m:
        n-=m
    else:
        m-=n
print("HCF of",p,"and",q,"is :",n)