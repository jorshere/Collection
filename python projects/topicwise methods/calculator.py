def calculator():
    global x,y,z
    x = int(input("enter 1 for addition 2 for subtaction 3 for multipy and 4 for division :"))
    if x<1 or x>4:
        print("'invalid selection")
        exit()
    y= int(input("input numbers:"))
    z= int(input("2nd number: "))

    if x==1:
         print(add(y,z))
    if x==2:
         print(sub(y,z))
    if x==3:
         print(mul(y,z))
    if x==4:
         print(div(y,z))
def add(n,m):
    return n+m
def sub(n,m):
    return n-m
def mul(n,m):
     return n*m
def div(n,m):
    return n/m
calculator()
