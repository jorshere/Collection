'''Binary Search:
            * For Binary Search, the elements of the list should be shorted in increasing order;
            * There will be Lower and Upper bound iin the sequence;and we have to find the mid-term;
                 If the mid term is equal to the searching number then print it OR Make the mid-term
                    next upper or lower bound   ;
'''
def bin_search(my_list,num):
    global pos
    LB= 0
    UB =len(my_list)-1
    for x in range(0,UB):
        mid= (LB+UB)//2
        if my_list[mid]==num:
            pos=mid+1
            return True
        elif my_list[mid] > num:
            UB=mid
        else:
            LB=mid
    return False


my_list=[]
N= int(input("enter the length of the list:"))
print("\n enter the element in your list in sorted order")
for i in range(0,N):
    val= int(input())
    my_list.append(val)

print("sorted list: ",my_list)
num= int(input("\nenter the element you are searching for: "))

if bin_search(my_list,num):
    print("your number found at   pos:",pos)
else:
    print("sorry,,, Not found")