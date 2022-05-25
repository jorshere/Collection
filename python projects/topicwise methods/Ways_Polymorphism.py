'''Polymorphism:  POLY-> many       MORPHISM-> forms
                    --->One that can take multiple forms;

    Uses for     : loose coupling, dependency injection, interfaces;

    Ways of doing Polymorpyism: 1) Duck typing
                                2) Operator overloading
                                3) Method Overloading
                                4) Method Overriding
    '''
print(".....................Duck Typing.........................")
class men:
    def execute(self):
        print("im half")

class women:
    def execute(self):
         print("other half")
    def __init__(self):
        print("women init here")

class boy:
    def crow(self,ideaa):             #   Duck Typing
        ideaa.execute()

ide1= men()
ide2 = women()
b1=boy()
b1.crow(ide2)                   # calling execute method by ide
print("\n\n.....................Operator Overloading........................")

"""When you compute a value or do operations; Python in back-end compute them with several inbuild methods and
        then overload it with the given input operator..i.e called operator overloading
        
        there were several inbuilt method to do operations"""

class student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def __add__(self, othere):          #inbuilt method for addition
        tm1= self.m1+self.m2+self.m3
        tm2= othere.m1+othere.m2+othere.m3
        s3= tm1+tm2
        return s3
    def __gt__(self, other):                    #  Wrong syntex
        t1= self.m1+self.m2+self.m3
        t2= other.m1+other.m2+other.m3
        return t1>t2
s1= student(3,6,6)
s2= student(6,10,5)
s4 =student(1,2,3)
s3=s1+s2                      # Since, we cant defined "+" operator in class, we have to use inbuilt method;
print(s3)
s5= s2+s4
print(s5)
print(type(s1))
print(type(s5))
if s1>s2:
    print("yes")
else:
    print("noooo")
print("\n\n....................Method Overloading And Overriding...................................")

'''Method Overloading: this way of polymorphism is not supported in Python ,thats why we have
                        to pass it manually.
                    for ex: what if there is three argument to pass but the user giving less then 3 input;
                        We dont have any method for that thats why we have to overload it 
   
    Method Overriding: if parents and child class both have same method; It will always priorities to child class
                    i.e method overriding;
'''
class X:
    def __init__(self):
        pass
    def mulo(self,a=None,b=None,c=None):                # Method Overloading
        s=0
        if a!=None and b!=None and c!=None:
            s= a+b+c
        elif a!=None and b!=None:
            s= a+b
        else:
            s= a
        return s

x1=X()
print(x1.mulo(3,2))     # what if we wont pass three argument

