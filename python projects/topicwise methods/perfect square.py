#import math as m
def perfsqur():
    global x,y
    x = int(input("enter the range of number: "))
    y = int(input())
    number= "there are {} perfect sqr no.s : "
    fun()
    print(number.format(a))
    print(seat)
    print("no more")
def fun():
    global a,seat
    a=0
    seat=[]
    for i in range(1,y+1):
        if i**2>=x and i**2<=y :
            seat.append(i**2)
            a+=1
perfsqur()
print("lol")
    
