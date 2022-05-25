'''Thread [multiThreading]:-
            Thread is as a light weight processes;
            when you breakdown big tasks into small parts, each part states as Thread;
            * By default every execution have one thread "Main Thread" , by this we can create more sub threads
        WE HAVE TO IMPORT THREADING TO PERFORM IT;

    run(self): inbuilt method to execute two different thread simultaneously;
            to call run() method we use "start()" method

    collision: If two threads are running simultaniously, there might be chance that they collide...
                thats why we use time delays;

    Time delay: to import time delay we have to import time;
                for delay in time we can use "sleep()" method


'''

from threading import *
from time import *

class even(Thread):
    def run(self):                  #inbuilt method to run simultaneously
        print("even numbers:")
        for i in range(2,21,2):
            print(i)
            sleep(3)

class odd(Thread):
    def run(self):
        print("odd series:")
        for i in range(1,20,2):
            print(i)
            sleep(3)

o= odd()
e= even()
o.start()               # to call "run()" method;
sleep(3)
e.start()

o.join()                 # for Main thread to let the sub thread join and then execute further;
e.join()
print("bye")


