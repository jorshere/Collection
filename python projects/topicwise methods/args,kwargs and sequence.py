"""  *args() operator and **kargs() keword argument AND Sequense of parameters:
    *args:
           * If you dont know the number of argument you want to pass , you can use *args()
           * It will assign all the values in a list;
           * It can also be used as parameter argument;

    **kargs:
             * same as *args, it will just store all the values to a dictionary;
             *  it will assign all the values in a dictionary;
             * It is also can be used as parameter;

    Sequence:  "PADK":  1) Normal parameters                2) *args()
                        3) Default parameters               4) **kargs()

            Suppose If you want to use all the parameters in your fun(), you can follow the above sequence
            for correct syntex;
"""

def example1(num,*args):
    print(args)
    x=0
    for i in args:
        x+=i
    print(f"given num: {num} and above sum: {x}")

#example1(5,45,65,756,75,34)


def example2(x,*args):
    for i in args:
        print(i)
    print(f"{x} : is given default")

num= {2,3,45,"shyam","Sram"}
#example2("con",*num)                # *args operator as parameter for unpacking the list otherwise it will take whole as list;


# **kargs():  when you have to pass a dictionary as parameter;

def example3(mega,**mego):
    for i,j in mego.items():
        print(f"{i} : {j}")
    print(mega)
hi = "ten"
my_dict= {"mix" : 1 ,"hite" : "song"}       # defining dictionary;
#example3(hi,**my_dict)                      # unpacking of dictionary ; Otherwise an error will occur;


# Sequence ( PADK ) :

def all_parameters(n_para,*args,def_para ='unknown',def_para2='known',**kwargs):
    print(n_para)
    print(args)
    print(def_para)
    print(def_para2)
    print(kwargs)
gender=["male","female"]
all_parameters(gender,26,"aug",1995,def_para2="brown",f_name= "Mr",l_name= "thanos")
'''
OUTPUT:
male
(26, 'aug', 1995)
unknown
brown
{'f_name': 'Mr', 'l_name': 'thanos'}'''


