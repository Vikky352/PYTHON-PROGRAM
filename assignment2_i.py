import cmath
n=complex(input("enter complex number (a+bj): "))
if n.real>n.imag:
    print(n.real,"real number is geatest number")
else:
    print(n.imag,"imaginary numberis geratest number")