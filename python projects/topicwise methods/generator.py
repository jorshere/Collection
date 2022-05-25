'''  GENRATOR:

'''
def top():
    yield (567,345)
    yield 4
    yield 5

def perf_sq():
    n=1
    print("perfect Square numbers:")
    while n <= 10:
        x= n*n
        n+=1
        yield x                 # Generator ... works as iterator

t=top()
print(t.__next__())
for x in t:
    print(x)
ps= perf_sq()
for i in ps :
    print(i)
