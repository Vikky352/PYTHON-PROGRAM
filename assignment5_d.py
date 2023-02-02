a=int(input("enter first number:"))
b=int(input("enter second number :"))
print("square of",a,"to",b,"will be :")
for j in range(a,b+1):
    s=j*j
    print(s,end=' ')
    s=0