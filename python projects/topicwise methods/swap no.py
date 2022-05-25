def swap():
    x=int(input("enter no1: "))
    y=int(input("enter no.2: "))
    x=x^y # xor gate
    y=x^y
    x=x^y
    print("swaped no: ")
    print(x)
    print(y)
swap()
