n=int(input("enter first number: "))
m=int(input("enter second number: "))
if n>m:
    max=n
else:
    max=m
while 1:
    if max%n==0 and max%m==0:
        print("Lcm of",n,"and",m, "is:",max)
        break
    max+=1