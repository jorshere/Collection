class Iterate:
    def __init__(self):
        print("Even numbers :")
    def __iter__(self):             # Inbuilt Iter method
        self.a=5
        return self
    def __next__(self):             # Inbuilt __next__ method
        if self.a <= 20:
            x=self.a
            self.a+=2
        else:
            raise StopIteration
        return x

class Iterate2:
    def __init__(self):
        print("Odd numbers:")
    def My_iter(self):
        self.a= 1
        return self
    def My_next(self):          # manually defining next method but for looping you have to use inbuilt methods
        if self.a <= 20:
            x= self.a
            self.a+=2
            return x
        else:
            raise StopIteration


i1= Iterate()
it1= iter(i1)               # to call __iter__ method
print(next(it1))             # to call __next__ method OR  (  print(it1.__next__())  ),,

next(it1)                   # if you dont want to print iteratable value
print(next(it1))
for i in it1:               # Iteration syntex for the method __next__
    print(i)


i2= Iterate2()              #self defined class and methods
i2.My_iter()
print(i2.My_next())          # way to print
print(i2.My_next())
print(i2.My_next())
