t1=eval(input("enter values to tuple: "))
t2=eval(input("enter values to tuple: "))
r=t1 if len(t1)<len(t2) else len(t2)
for i in range(r):
    c=0
    if t1[i] != t2[i]:
        c+=1
if c==0:
    print("elements of tuple are in same order")
else:
    print("elements of tuple are not in same order")
