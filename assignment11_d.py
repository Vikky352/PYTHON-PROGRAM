def word(a):
    c=0
    for i in a:
        if i!= ' ':
            c+=1
    return c       
s=input("Enter word: ")
d=word(s)
print("Total number of word in '%s' is:"%s,d)