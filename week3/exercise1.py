import functools

@functools.lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


# generator function is a way to change state in the fly
# this way we can save memory
# because it doesn't store all the values in memory
# it only stores the current value

# any operation is happens is done in the second value
# you can yeild multiple times in a function



def fibo_gen(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b



for i in fibo_gen(10):
    print(i)