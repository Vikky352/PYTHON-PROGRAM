x=int(input("enter number:-"))
x=x+1
for j in range(x,x+10):
    c=0
    
    for i in range(2,10):
        if j%i==0:
         c=c+1
    if c==0:
        break
print("next prime number is %d"%j)