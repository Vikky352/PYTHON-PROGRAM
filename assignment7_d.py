s=input("enter string: ")
l=len(s)
r=s[0]
for i in range(l):
    if s[i] not in r:
        r=r+s[i]
print("occurance of given character in given string:")
for j in range(len(r)):
    c=0
    for k in range(l):
        if r[j]==s[k]:
            c+=1
    print(r[j],c)
        