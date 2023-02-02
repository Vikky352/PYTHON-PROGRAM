def dic(l):
    d={}
    for j in range(len(l)):
        c=0
        for i in l:
            if l[j]==i:
                c+=1
        d[l[j]]=c
    return d

l=eval(input("enter element to add: "))
r=dic(l)
print("value"," ","frequency")
for key,value in r.items():
     print(" ",key," - ",value)