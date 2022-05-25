# use of __init__ function;
from buffer import *
def fun1():
    print(__name__)
    gam()
    print("aeae")
def fun2():
    print("name222")
def maino():
    fun1()
    fun2()

maino()