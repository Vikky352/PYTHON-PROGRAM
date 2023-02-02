from itertools import combinations
def combination(p):
    q=2
    return list(combinations(p,q))

l=int(input("Enter term to add: "))
s1=set()
print("Enter first set %d element:"%l)
for i in range(l):
    s1.add(int(input()))
t=combination(s1)
print("All possible subset:\n",t)