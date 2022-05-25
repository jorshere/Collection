'''METHODS: three types of methods->
             1) Instanse method :  methods defined inside methods are class.
             2) class method :  works with class variables,  For defining a classs method we have to use
                        a decorator (@classmethod).
             3) Static method : Something extra or diffrent than instanse and class method,
                                If we have to perform operation wit other class object'
                                decorator is used (@staticmethod)
'''

class fruits:
    taste = "sweet"
    def __init__(self):
        self.name= "apple"
        self.quantity = "1kg"
    def show(self):
        print(self.name,self.quantity,self.taste)
    def get_name(self):                                 #Instanse methods
        return self.name
    def set_qua(self,value):                             #Instanse method
        self.quantity=value
    @classmethod
    def sources(cls):           #(cls) : inbuilt method to releate it to class.
        return cls.taste

    @staticmethod
    def infor():
        print("free delivery over 10kg")

f1= fruits()
f2= fruits()
f2.name="grapes"

f1.show()
fruits.taste= "sour"                    # changing value of class variable
f2.show()

print(f1.get_name())
f1.set_qua("2kg")
f1.show()
print(fruits.sources())             # calling class method;
f1.show()
f1.infor()                          # calling static method:

# Q) have to experiment with static methods