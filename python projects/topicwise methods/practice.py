from buffer import *
def calc():
    z = float(input("enter the 1st no.: "))
    c = float(input("enter 2nd value: "))
    x= int(input("select operantion: "))
    if x==1:
        print(add(z,c))

    else :
        print("invalid selection")

calc()
