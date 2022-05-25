"""def armstrong_range(a,b):
    global t,sum
    t=[]
    for x in range(a,b+1):
        p= len(str(x))               #length of number;
        u=p
        temp=x
        sum=0
        while u > 1:
            temp2=temp%10
            sum+=temp2**p
            temp//=10
            u-=1
        if sum==x:
            t.append(sum)

o=int(input("enter the range of no. between you want armstong nos.:"))
i=int(input("enter end range: "))
armstrong_range(o,i)
print("the list of armstrog no.: ")
print(t)"""
def armstrong(n,r):
    global series
    series=[]
    if n<=0 :
        series.append("0")
    if n<=1:
        series.append("1")
    for h in range(n,r+1):
        s = len(str(h))
        p=int(s)
        temp = h
        result = 0
        if p > 2:
            while p > 0 :
                temp2 = temp % 10
                 # print(temp2)
                result += temp2 ** s
                # print(result)
                temp //= 10
                p-=1
            if result == h:
                series.append(result)
        # else:
#        print("sorry!!!!")

a = int(input("enter starting range for armstrong no.: "))
b= int(input("end range : "))
armstrong(a,b)
print(series)