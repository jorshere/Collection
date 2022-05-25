# filter() , map(), reduce() functions....
# for big data concent: for a junk of data ; apply filter() to extract useful data;
# map() to apply certain operation on the list; reduce() to get reduced outcome;
from functools import reduce
nums= [2,4,12,54,6,3,9,57,37,53]
def is_odd(n):
    return n%2==1

odd=list(filter(is_odd,nums))          # filter() used to filter the element from the collection via diff. conditions;
print(odd)


                                            #       OR....by using lambda;
even=list(filter(lambda a: a%2==0,nums))
print(even)
print("filter is over")

def mux(n):
    return n*n
odd_sqr = list(map(mux,odd))            # using map() to square the list;
print(odd_sqr)

even_sqr=list(map(lambda n: n*n,even))
print(even_sqr)       #  OR by using lambda;
print("mapping over")


def sum(a,b):
    return a+b
odd_sum=reduce(sum,odd_sqr)        # using reduce() to add all values in list and make single element;
print(odd_sum)                      # required to import reduce from functools;

even_sum= reduce(lambda a,b:a+b,even_sqr)        #   using lambda
print(even_sum)
print("reducing complete")