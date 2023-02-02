def cube(n):
    if n==1:
        return 1
    return n*n*n + cube(n-1)
n=int(input("Enetr number of term: "))
r=cube(n)
print("First %d natural number cube sum:"%n,r)