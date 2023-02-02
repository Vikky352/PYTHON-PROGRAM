l=[]
n=int(input("enter number of term you want: "))
for i in range(n):
    l.append(int(input()))
l1=[]
l1.append(l[0])
for i in range(1,len(l)):
    if l[i] not in l1:
        l1.append(l[i])
for i in l1:
    c=0
    for j in l:
        if i==j:
            c+=1 
    print(i,c)