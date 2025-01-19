class test:
    x=10    #static variable.
    def __init__ (self): #constructor using double underscore.
        self.a=100    #self is like "this" keyword
    #   print(t1.a)
        self.b=120
        test.y=400  #static variable
        print(id(self))
    def m1(self):
        self.c=30
        print("hi",id(self.c))
        self.d=40
    @classmethod
    def m2(cls):
        cls.f=60
        test.g=60
t1=test() #creating object in python
print(id(t1))
print(t1.a)
t1.m1()
print(t1.__dict__)
del t1.d
print(t1.__dict__)  # gives how many variable are initialized.
t2=test()
t2.m1()
t1.c=300  #300,30 is object initialized in variable c.
t1.m2
print(t1.__dict__)
print("bye",id(t1.c))
print(t1.__dict__)
print("static variable: ",t1.x,t1.y)    #static variable printing
print(t1.__dict__)  #static variable:  10 400 {'a': 100, 'b': 120, 'c': 300} static variable is not associated to objebt
t1.m1()
print("here",t1.__dict__)
                    #'@' is used as annotation. method defined using @ is static method. and that method does not belong to object. 
def m2(cls):
    cls.f=60
    test.g=60
t1.m2
print(t1.__dict__)
class test:
    a=10
    def __init__(self):
        print(self.a)
        print(test.a)
    def m1(self):
        print(self.a)
        print(test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(test.a)
    @staticmethod
    def m3():
        print(test.a)
t=test()
print(t.a)
t.m1()
t.m2()
t.m3()
print(t)
print(id(test))
t.a=1000000000000
print(t.a)
del test.a
print(t.__dict__)
print(test.__dict__)

class test():
    a=10
    def __init__(self):
        self.b=20
t1=test()
t1.a+=2
print(t1.a)
print(test.a)

class test:
    a=10
    def __init__(self):
        self.b=20
        test.c=30 
    def m1(self):
        self.d=40
        test.e=50  
    @staticmethod
    def m3():
        test.a=40

print(test.a)
print(test.__dict__)  
t=test()
print("association with t:",t.__dict__)
t.m1()
print(t.__dict__)
print(test.__dict__)
t.m3()
print(test.a)
        
def  university():
    branch=input("Enter your branch: ")
    def __init__(self):
        self.branch="cse"
    @staticmethod
    def x1():
        university.branch="AI"
x=university()
x.x1()
print(university.branch)
----------------------------------------------------------------------------------------------------------------------
class university:
    university_name=input("Enter name of university: ")
    def __init__(self):
        self.student_name=input("Enter your name: ")
        self.erp=int(input("enter your enrollment number: "))
        self.phone=int(input("Enter your phone number: "))
        print(F"all the details are: \n{self.student_name}\n{self.erp}\n{self.phone}")
n=int(input("how many student entries?"))
for i in range(n):
    x=university()
---------------------------------------------------------------------------------------------------------------------------------------------
class university:
    university_name=input("Enter name of university: ")
    def __init__(self,student_name,erp,phone):
        self.student_name=student_name
        self.erp=erp
        self.phone=phone
        print(f"all the details are: \n{self.student_name}\n{self.erp}\n{self.phone}")
n=int(input("how many student entries?"))
for i in range(n):
    student_name=input("Enter your name")
    erp=int(input("enter your ERP"))
    phone=int(input("enter phone number"))
    x=university(student_name,erp,phone)
    
----------------------------------------------------------------------------------------------------------------------------------
a=100

class test:
    a=111
    def m1(self):
        print(a)         #global variable
        print(self.a)       #local variable/class variable.
t=test()
t.m1()

or

class test:
    def m1(self):
        global x
        x=111
        print(x)         #global variable
    def m2(self):
        print(x)       
t=test()

t.m1()
t.m2()

class student:
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("enter no of students: "))
for i in range(n):
    name=input("enter name: ")
    marks=int(input("enter your marks: "))
    s=student()
    s.setname(name)
    s.setmarks(marks)
    print(s.getname())
    print(s.getmarks())
---------------------------------------------------------------------------------------------------------------
class test:
    def property(self):
        print('cash+land+gold+power')
    def fun(self):
        print('have fun')
        
class C(test):
    def fun(self):
        super().fun()
        print('lots of fun')
class D(C):
    def fun1(self):
        super().property()
        print('not goodd')
c=C()
c.property()
c.fun()
d=D()
d.property()
d.fun1()
t=test()
t.property()
t.fun()

method overloading example
class sum1:
    def sum_of_two(self,*n):
        return sum(n)
s=sum1()
print(s.sum_of_two(1,2))
print(s.sum_of_two(1,2,4))
print(s.sum_of_two(1,2,4,5))
-------------------------------------------------------------------------------------------------------------------------



