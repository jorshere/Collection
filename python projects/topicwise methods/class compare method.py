class student :
    def __init__(self):
        self.name= "Jors"
        self.clsw = "12 b"
        self.roll = 23
    def update(self):
        self.roll= "11"
    def compar(self,xyz):
        if self.roll == xyz.roll:
            print("yep bro")
        else:
             print("nop bro")


s1 = student()
s2 = student()

s1.name="Raj"
s1.clsw= "11 b"
s1.roll = 23

s1.compar(s2)
s1.update()                          # to update any object
s1.compar(s2)

