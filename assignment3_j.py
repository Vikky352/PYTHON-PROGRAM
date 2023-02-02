n=int(input("enter number of term :-"))
x=1
s=1
c=1
while c<=n:
    if x%2!=0:    
        s=s*x
        c=c+1
    x=x+1
print("product of first %d odd natural numbers are :- %d"%(n,s))
