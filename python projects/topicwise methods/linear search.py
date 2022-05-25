'''Linear Search:
            In linear search, we search for data one by one by compairing each element with the matching data

'''

def lin_search(my_list,num):
    global pos
    x=0
    while x< len(my_list):
        if my_list[x] == num:
            pos= x+1
            return True
        x+=1

# Input of the list
my_list= []
n = int(input("enter the length of your list:"))
print("\n enter the element in the list")
for i in range(0,n):
    val = int(input())
    my_list.append(val)
print("\n",my_list)
num = int(input("\n enter the no. you want to search for:"))

# method for linear search
if lin_search(my_list,num):
    print("number found at:   pos",pos)
else:
    print("nunber not found")

