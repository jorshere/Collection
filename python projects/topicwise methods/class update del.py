class student :
    def __init__(self):
        self.name= "Jors"
        self.clsw = "12 b"
        self.roll = 23
    def update(self):
        self.clsw= "12 a"


s1 = student()
s2 = student()

s1.name="Raj"
s1.clsw= "11 b"
s1.roll = 11

print(s1.clsw)
s1.update()                          # to update any object
print(s2.clsw)
print(s1.name)
s1.clsw = "13 c"
print(s2.clsw)
print(s2.name)
#del s1                       to delete any class
print(s1.clsw)