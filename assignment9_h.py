from itertools import combinations
l=int(input("Enter term to add: "))
s1=[]
print("Enter first set %d element:"%l)
for i in range(l):
    s1.append(input())
r=int(input("Enter no of subset combination : "))
print("All possible subset:\n",list(combinations(s1,r)))