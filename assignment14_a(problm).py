class student:
    def __init__(self,roll,name,sem,branc):
        self.roll=roll
        self.name=name
        self.sem=sem
        self.branc=branc

s1=student(101,'rohan',3,'b.tech')
s2=student(102,'ravi',4,'mca')
print(s1.roll,s1.name,s1.sem,s1.branc)
print(s2.roll,s2.name,s2.sem,s2.branc)