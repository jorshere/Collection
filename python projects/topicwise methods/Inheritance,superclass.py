'''Iheritance : Constructor in Inheritance::  If you create an object of child class , first it will try to find
                __init__ of sub class, then after go for own __init__. If commad prvided, then it can
                 access his own methods:

                 Super().__init__:: call features of the parent class

                 '''


class A:
    def __init__(self):
        print("A in init")
    def clue(self):
        print("first clue")
    def clue2(self):
        print("second clue")
class B(A):
    def __init__(self):
        super().clue2()
        print("B in init")
        #super().__init__()                   # to call parent class __init__ fun
    def clue3(self):
        print("third clue")
    def clue4(self):
        print("forth clue")
class C(B):
    def __init__(self):
        super().__init__()    # parnt class selection biased over left to right seq.
        A.clue2(self)               # to call particular class
        print("C in init")
    def clue5(self):
        print("final clue")
b1=B()
a1 = A()
#b1=B()
#c1=C()