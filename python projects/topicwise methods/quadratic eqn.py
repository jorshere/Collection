import cmath                # for the complex numbers(ex: 3+4j)
a= float(input("input values for quadratic euation: "))
b= float(input())
c= float(input())
d= b**2-4*a*c
sol1 = (-b+cmath.sqrt(b))/2*a
sol2 = (-b-cmath.sqrt(b))/2*a
print("there will be two soltions... those are {} and {}".format(sol1,sol2))
