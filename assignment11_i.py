def dic(l):
    d={}
    for j in l:
        s=j[0]
        d[s]=j
    return d

l=int(input("enter element to add: "))
s=[]
for i in range(l):
    s.append(input())
r=dic(s)
for key,value in r.items():
     print(key,"-",value)