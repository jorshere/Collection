"""List Comprehension:
            * with the help of this we can create a list in single line;
   ex: listed below
"""
# to create list of cubes;
cube1=[]
for i in range(1,11):       # simple for loop
    cube1.append(i**3)
#print(cube1)

cubes = [x**3 for x in range(1,11)]         # by list comprehension;
print(cubes)

# to print negative values of list;

print([-i for i in range(1,11)])

# to print first letter of the elements:

names= ["Jors","Mors","Tcors"]
first_letter=[i[0] for i in names]
print(first_letter)


# to reverse a list :

def rev_listing():
    num= int(input("enter the length of your list:"))
    print("enter the element in your list:\n")
    my_list = [input() for i in range(num)]
    print(my_list)
    print("the reverse list be:\n")
    revr_list = [ i[::-1] for i in my_list]
    return revr_list

#print(rev_listing())

# If statement in list comprehension;

even_num = [k for k in (range(1, 11)) if k%2 == 0 ]
print(even_num)         # to get even values;

# to find int() and float() elements and return list with strings.
ion =["mega","line",34,4.5,1,"rohan",True,False]
print([i for i in ion if type(i) == int or type(i) == float])

# If-Else statement..
    # OUTPUT: [1,-2,3,-4,5,-6,7,-8,9]



# Nested If-Else:

y = [False,13.4,"mixture",78.6,"john",[1,3,5],"mask",45,64,True,False]

ml = [ i if (type(i)== bool) else (i*1.7 if (type(i)== int or type(i)==float) else (i.capitalize()+"-chan" if (type(i)==str)else type(i) ))  for i in y]
print(ml)

#Output:  [False, 22.78, 'Mixture-chan', 133.61999999999998, 'John-chan', <class 'list'>, 'Mask-chan', 76.5, 108.8, True, False]





nuxx = [-i if (i%2==0) else i for i in range(1,10)]
print(nuxx)

# Nested list comprehension;
pattrn= [["*" for i in range(0,j)] for j in range(1,4) ]
print(pattrn)

nested_list = [[i for i in range(1, 4)] for j in range(0, 3)]
print(nested_list)

