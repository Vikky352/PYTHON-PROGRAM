n=int(input("enter number greater than 9:-"))
c=0
for i in range(2,10):
    if n%i==0:
        c=c+1
if c==0:
    print("%d is prime number "%n)
else:
    print("%d number is not prime"%n)