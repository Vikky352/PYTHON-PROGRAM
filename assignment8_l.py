t=eval(input("enter values to tuple: "))
c=[]
c.append(t[0])
for i in range(1,len(t)):
    if t[i] not in c:
        c.append(t[i])
t1=tuple(c)
print("Number","Frequency")
for i in t1:
    c1=0
    for j in t:
        if i==j:
            c1+=1    
    print("",i,"  ",c1)