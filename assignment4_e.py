from re import I


a=int(input("enter first number: "))
b=int(input("enter second number: "))
i=2
c=0
while i<10:
    if a%i==0 and b%i==0:
        c+=1
    i+=1
    
if c==0:
    print("both number are co-prime number")
else:
    print("both number are not co-prime number")
        