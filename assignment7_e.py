s=input("enter string: ")
l=len(s)
c=0
for i in range(l):
    if s[i]!=' ':
        c+=1
print("number of character in string:",c)