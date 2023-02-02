l=int(input("Enter term to add: "))
s1=[]
print("Enter first set %d element:"%l)
for i in range(l):
    s1.append(input())
s=set(s1)
print("total distinct element in list :",len(s))
