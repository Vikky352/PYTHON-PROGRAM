t=eval(input("enter values to tuple1: "))
c=[]
c.append(t[0])
for i in range(1,len(t)):
    if type(t[i])==type(t[0]):
        c.append(t[i])
t1=tuple(c)
print(t1)