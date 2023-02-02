print("armstrong under 1000 will be :")
for i in range(1,1000):
    s=0
    j=i
    while(i>0):
        r=i%10
        p=r*r*r
        s=s+p
        p=0
        i=i//10
    if s==j:
        print(s)
   