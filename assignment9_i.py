l=int(input("Enter term to add: "))
s1=[]
s2=[]
print("Enter first set %d element:"%l)
for i in range(l):
    s1.append(input())
print("Enter second set %d element:"%l)
for i in range(l):
    s2.append(input())
    s=[]
for i in s1:
    for j in s2:
        l=[]
        l.append(i)
        l.append(j)
        s.append(l)
print(s)        


# we will print cartesian product with function
#   from itertools import product
#       print(list(product(s1,s2)))