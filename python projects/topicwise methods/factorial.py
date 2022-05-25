def facto():
    fact= int(input("input a number: "))
    n=1
    for x in range(1,fact+1):
       n= x*n
    print("the factorial is :",n)
facto()