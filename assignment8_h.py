t1=eval(input("enter values to tuple: "))
t2=eval(input("enter values to tuple: "))
for i in t1:
    c=0
    if i not in t2:
        c+=1
        break
if c==0:
    print("tuple containing same element")
else:
    print("tuple not containing same element")