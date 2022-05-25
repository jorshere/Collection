'''VARIABLE: two types of variable->
 1) Instanse variable : variables defined inside methods are instanse variable.
 2) class/ static variable :  ie defined inside class and common to all object.
'''

class fruits:
    taste = "sweet"      # class/static variable
    def __init__(self):
        self.name= "apple"                  # instanse
        self.quantity = "1kg"               #          variables
    def show(self):
        print(self.name,self.quantity,self.taste)

f1= fruits()
f2= fruits()
f2.name="grapes"

f1.show()
fruits.taste= "sour"                    # changing value of class variable
f2.show()
f1.show()