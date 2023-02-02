x=int(input("enter first number:- "))
y=int(input("enter second number:- "))
z=int(input("enter third number:- "))
if x>y>z:
    print("%d is greatest number"%x)
elif y>z:
    print("%d is greatest number"%y)
else:
    print("%d is greatest number"%z)