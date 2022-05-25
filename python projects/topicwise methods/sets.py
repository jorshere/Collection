"""Set:
        *    It is a collection of unordered and unindexed elements
        *    represented as {} ...
        *    doesn't support duplicates; thats why we can use it to remove duplicates;
        *    supports maths() set functions i.e  union() and intersection().

"""
my_set = {1, 32, 43, 36.5, 76.02, 'thanos', "mj", 25, 90}
lis = [1, 2, 3, 3, 5, 45, 65, 45, 8, 9, 9, 7, 87, 98, 876, 67, 87, 5, 65]

print(list(set(lis)))  # to remove duplicates from list.

my_set.add(89.76)  # to add items to set

my_set.pop()               # to pop an element

my_set.remove(90)  # to remove any item , it given item not present it will give error.

my_set.discard("jokar")  # it will remove item, but doesn't show error if element missing,
print(my_set)

# my_set.clear()         # to clear the set

set1= {1,2,3,4,5,6}
set2 = {3,4,5,6,7,8,9}

union_set = set1 | set2     # for union of two set;
print(union_set)

intersection_set = set1 & set2      # for intersection of two set
print(intersection_set)
