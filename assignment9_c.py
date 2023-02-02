l=int(input("Enter term to add: "))
s1=set()
s2=set()
print("Enter first set %d element:"%l)
for i in range(l):
    s1.add(input())
print("Enter second set %d element:"%l)
for i in range(l):
    s2.add(input())
r=s1.union(s2)
print("Union between two set:",r)

