from threading import *
import time


class MyThread1(Thread):
    def run(self):
        print("This is MyThread 1")
        for i in range(1, 11):
            print(f"\nMy Thread1: {i}")
            time.sleep(1)


class MyThread2(Thread):
    def run(self):
        print("This is MyThread 2")
        for i in range(1, 11):
            print(f"\nMy Thread2: {i}")
            time.sleep(1)


if __name__ == "__main__":
    print("\nMain Thread Start. . .")
    t1 = time.time()

    # creating threads
    trd1 = MyThread1()
    trd2 = MyThread2()

    # starting threads
    trd1.start()
    trd2.start()

    print(f"\nActive Threads = {active_count()} i.e Main Thread, Thread 1 and Thread 2\n")

    trd1.join()  # Wait for MyThread1 to finish
    trd2.join()  # Wait for MyThread2 to finish

    t2 = time.time()
    print(f"\nTotal execution time: {t2-t1}")

    print("\nMain Thread End. . .")
