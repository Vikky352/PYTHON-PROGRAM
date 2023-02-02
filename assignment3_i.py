n=int(input("enter number to calculate factorial:-"))
f=1
s=n
while n>=1:
    f=f*n
    n=n-1
print("factorial of %d is:-%d"%(s,f))