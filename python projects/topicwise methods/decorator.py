#  Decorator :  it changes the behavior of existing function, while in compilaton time;

def div(a,b):
    print(a/b)
def smart_div(fun):                 # using decorator... to divide larger to smaller no. only;
    def inner(a,b):
        if a<b:
            a,b=b,a
        return fun(a,b)
    return inner

x=int(input("enter a number :"))
y=int(input("2nd number:"))
div=smart_div(div)
div(x,y)