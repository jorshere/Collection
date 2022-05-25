
import numpy
n=int(input("enter the number:"))
a=[]
while n>1:
    x=n%2
    a.append(x)
    n=n//2
a.reverse()
#x=int(a)
print("binary conversion:  ",end='')
print (n,end='')
for i in a:
    print(i,end="")
#print (i+2)
