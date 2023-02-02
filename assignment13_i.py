def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
n=int(input("Enter number of term: "))
print("First %d fionacci are:"%n)
for i in range(n):
    print(fib(i)) 