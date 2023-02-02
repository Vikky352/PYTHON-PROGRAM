l=eval(input("Enter value to in set 1: "))
l1=eval(input("Enter value to in set 2: "))
s1=set(l)
s2=set(l1)
if s1.issubset(s2):
    print("s1 set is subset of set s2")
elif s2.issubset(s1):
    print("s2 set is subset of set s1")
else:
    print("no any set is not subset of another set")