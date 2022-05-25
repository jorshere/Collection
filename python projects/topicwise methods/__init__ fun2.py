class mod :
    def __init__(self,model,cost,color):
        self.model= model
        self.cost= cost
        self.color= color
    def stats(self):
        x= "Model is {} , Cost {} , Color {} "
        print(x.format(self.model,self.cost,self.model))

c1 = mod('t21',560000,'blue')
c2= mod('prt231',100000,'white')
c3 = mod('bmv123',2800000,'grey')

c1.stats()
c2.stats()
c3.stats()