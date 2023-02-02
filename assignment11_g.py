def fibo(p):
    x=0
    y=1
    z=0
    s=[]
    while p>0:
        s.append(z)
        z=x+y
        y=x
        x=z
        p-=1
    return s
        
l=int(input("Enter number of term: "))
f=fibo(l)
print(f)