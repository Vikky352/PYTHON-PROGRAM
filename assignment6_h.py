l=[]
n=int(input("enter number of term you want: "))
for i in range(n):
    l.append(int(input()))
e=0
o=0
for i in l:
    if i%2==0:
        e+=i
    else:
        o+=i
print("sum of all even numbers from list  are :",e)
print("sum of all odd numbers from list are :",o)
