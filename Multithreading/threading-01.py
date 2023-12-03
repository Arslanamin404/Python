# Threading without class

from threading import *


def show():  # creating a function
    for i in range(1, 11):
        print(i)


def display():
    for i in range(100, 111):
        print(i)


# creating thread
trd1 = Thread(target=show)
trd2 = Thread(target=display)

trd1.start()  # starting the thread 1
trd2.start()  # starting the thread 2

# waiting until thread 1 is done with the execution
trd1.join()

# waiting until thread 2 is done with the execution
trd2.join()

print("END")
