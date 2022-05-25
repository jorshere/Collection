'''Bubble Sorting:
            * sorting the list of element BY compairing each element with its preceeding element and the swaping it
'''
def bubble_sort(my_list,num):   # bubble sort loogic:
    for i in range(num-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp= my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp

my_list=[]
num= int(input("enter the length of the list for bubble sorting:"))
print("\nenter the element in the list:")
for k in range(num):
    run=int(input())
    my_list.append(run)

bubble_sort(my_list,num)
print(my_list)