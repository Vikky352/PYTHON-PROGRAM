import math as m
l=int(input("Enter term to add: "))
s1=[]
print("Enter first set %d element:"%l)
for i in range(l):
    s1.append(input())
l=len(s1)
l1=(int)(m.pow(2,l))
t1=[]
for c in range(0,l1):
    t=[]
    for i in range(0,l):
        if (c & (1<<i))>0:
            t.append(s1[i])
            if t not in t1:
                t1.append(t)        
print("powerset of guven set:\n",t1)