import math
a=int(input("enter first component:- "))
b=int(input("enter second component:- "))
c=int(input("enter third component:-"))
d=b*b-4*a*c
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("root of quadratic equation are %d &%d "%(r1,r2))
elif d==0:
    r1=-b/(2*a)
    r2=-b/(2*a)
    print("root of quadratic are %f and %f"%(r1,r2))
else:
    print("roots are imaginary")