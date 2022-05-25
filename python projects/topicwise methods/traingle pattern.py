def pattern():
    global a
    a = int(input("enter the height of triangle: "))
    for x in range(1,a+1):
        for z in range(1,x+1):
            print("*",end=" ")
        print("\r")
def pattern2():
    print("next one:")
    for x in range(a,0,-1):
        for z in range(0,x):
            print("*",end=" ")
        print("\r")
def pattern3():
    print("and  for the next one: ")
    to = a
    po = 1
    for y in range (0,a):
        for x in range(1,to):
            print(end=" ")
        to-=1
        for z in range(0,po):
            print("*",end="")
        print("\r")
        po+=2
pattern()
pattern2()
pattern3()


