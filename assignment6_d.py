l=[]
n=int(input("enter number of term: "))
i=2
c=0
while c<n:
    for j in range(2,i+1//2):
        if i%j==0:
            break
    else:
        l.append(i)
        c+=1
    i+=1
print(l)