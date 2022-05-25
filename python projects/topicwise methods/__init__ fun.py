#using __init__ function;;;;;;



class employee:
    def __init__(self,group,salary):         # it will call itself automatically.
        self.group= group
        self.salary= salary
    def sublist(self):
        print("art of it:",self.group,self.salary)
sub1=employee('A',80000)
sub2=employee('B',50000)
sub3=employee('C',25000)

sub1.sublist()
sub2.sublist()
sub3.sublist()