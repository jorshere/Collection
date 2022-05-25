'''ERROR in Python    [Exception Handling]:

        1) Compile time Error: which occur while compile time; Syntex error ; Wrong spelling etc.

        2) Logical Error:  cause due to wrong logic, ex: using wrong arithmetic operator for output;

        3) Runtime Error: hard to find; eg:  Divided by zero error.

'''
print("entering to the server\n")
try:
    a= int(input("enter 1st number: "))
    b= int(input("enter 2nd number:"))
    print(float(a/b))
except ZeroDivisionError as e:       # we can specify errors or make a universal syntax as Exception
    print("cant do",e)
except ValueError as e:
    print("cannot do",e)
except Exception as e:
    print(e)
finally:                # finally block will print even if there is any exception;
    print("Server closed")
print("byeeee")