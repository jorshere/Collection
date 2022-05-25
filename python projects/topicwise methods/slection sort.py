'''Selection Sort :
            * In this sorting technique we search for minimum value by comparing next element
                and finally swap first element with the minimum value;
            * the go for the next iteration;
 '''

def sele_sort(my_list,num):                 #seection sort logic:
    for i in range(num-1):
        minterm= i
        for j in range(i,num):
            if my_list[j] < my_list[minterm]:
                minterm= j

        temp= my_list[minterm]
        my_list[minterm] = my_list[i]
        my_list[i]=temp

    print("after selection sort:", my_list)

my_list=[]
num= int(input("enter the length of your list:"))
print("enter the elements for selection sorting :")
for i in range(num):
    run= int(input())
    my_list.append(run)
print("provided list",my_list)

sele_sort(my_list,num)
