s=input("enter string : ")
l=len(s)
r=s[0]
for i in range(1,l):
    if s[i] not in r:
        r+=s[i]
print("After removing duplicate element from string is:",r)