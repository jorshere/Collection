class teacher:
    def __init__(self,name,sub):
        self.name = name
        self.sub = sub
        #self.inr = self.info()
        #self.inr.gender="Female"
    def show(self):
        print("name of teacher: ",self.name,"\nsubject studies: ",self.sub)
        #self.inr.shown()
    class info :
        def __init__(self):
            self.gender= "Male"
            self.age =  21
        def shown(self):
            q2.show()
            if self.age > 20 :
                print(self.gender,self.age)
            else: print("hehe")

q1= teacher("raj","ENG")
q2= teacher("mohan","SCI")
q1.show()

'''lap1= q1.inr
lap2= q2.inr
lap2.shown()'''
lap1 = teacher.info()       # OUTside class defination
lap2 = q2.info()
lap2.gender="Trans"
lap1.shown()
lap2.shown()