''' INNER CLASS in Python:
            You can create an object of inner class inside outer class:
                    OR
            create object of inner class outside Outer class provided you use outer class name
            to call it:
'''

class tees:
    sleeve= "Full"
    def __init__(self):
        self.size= 40
        self.color ='blue'
        self.ptrn= self.pattern(2,4,53)                 #OBJECT for the inner class
    def show(self):
        print("size is:",self.size," \ncolor is: ",self.color)
        self.ptrn.syst()

    class pattern :                                             # INNER CLASS
        def __init__(self,plane,cube,circle):
            self.plane= plane
            self.cube= cube
            self.circle=circle
        def syst(self):
            print(self.plane,self.cube,self.circle)

t1= tees()
t2= tees()
t1.size= 38
t1.color = 'green'
t1.show()
print(t1.ptrn.circle)
#patt1= t1.ptrn
#patt2= t1.ptrn