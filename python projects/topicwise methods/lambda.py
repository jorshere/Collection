# Lambda: it is an anonymous function; when we want to pass an anonymous function we use lambda;
def squr(a):
    print(a*a)
squr(5)

#     OR

f= lambda a: a*a
print(f(8))

#      OR

g= lambda a,b,c,d: (a*b+c)%d
print(g(2,3,4,3))