def natural(n,i=0):
    i+=1
    if n==1:
        print(i)
        return
    else:
        print(i)
        natural(n-1,i)
n=int(input("Enter term you want: "))
print("First %d natural number is: "%n)
natural(n)