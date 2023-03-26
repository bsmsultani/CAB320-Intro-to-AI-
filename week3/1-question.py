# functools is a module that contains tools for working with functions

import functools

import time


# lru_cache is a decorator that caches the results of a function
# so that it doesn't have to be called again
# it is a way to save memory
# it is a way to save time
# it also allows faster computation when function is called recursively
@functools.lru_cache(maxsize=None)
def fibo_1(n):
    if n < 2:
        return n
    else:
        return fibo_1(n-1) + fibo_1(n-2)


# generator function is a way to change state in the fly
# this way we can save memory
# because it doesn't store all the values in memory
# it only stores the current value

def fibo_2(n):
    if n < 2:
        return n
    
    last_value = 1

    for i in range(n):
        last_value += i
        yield last_value


for i in fibo_2(10000000):
    print(i)