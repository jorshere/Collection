def armstrong(n):
      s= len(str(n))
      temp=n
      result=0
     # print (s)
      for x in range(0,s):
          temp2=temp%10
         # print(temp2)
          result+=temp2**s
         #print(result)
          temp//=10
      if result==n:
        print("no. is armstrong")
      else:
        print("sorry!!!!")

a= int(input("enter no. whether its armstrong or not: "))
armstrong(a)