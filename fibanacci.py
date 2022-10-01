from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        time_taken = t2 - t1
        print(time_taken/1000)
    return wrapper


@performance
def fib(limit):
    num1 = 0
    num2 = 1
    for i in range(limit):
        total = num1+num2
        # print(total)
        num1 = num2
        num2 = total


@performance
def fib2(limit):
    num1 = 0
    num2 = 1
    for i in list(range(limit)):
        total = num1+num2
        # print(total)
        num1 = num2
        num2 = total


fib(20000)
fib2(20000)
