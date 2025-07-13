import time


def timer(func):
    def inside_func(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        fn = time.time()
        print(f"Function {func.__name__} works {fn - st} seconds")
        return fn - st

    return inside_func


@timer
def g(x, y, z):
    s = 0
    for i in range(x):
        for j in range(y):
            for z in range(z):
                s += i + j + z
                k = i ** j ** z


g(100, 100, 120)


@timer
def F(x):
    a = 100
    for i in range(100000000):
        a += i


print(F(10))


def cache(func):
    D = {}

    def inside_func(*args):
        if args not in D:
            D[args] = func(*args)
        return D[args]

    return inside_func


@cache
def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(55))
print(fib(10))
print(fib(5))


def logging(func):
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as f:
            f.write(f"Function {func.__name__} called with argument {args} {kwargs}")
        return func(*args, **kwargs)

    return wrapper


@logging
def sum(a, b, c):
    return a + b + c


sum(1, 2, 4)
sum(23, 51, 64)
sum(23, 51, 64)


def retry(max_attempts, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                result = func(*args, **kwargs)
                if result is not None:
                    return result
                attempts += 1
                time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(3, delay = 2)
def F(a,b):
    if a > b:
        return None
    else:
        return a*b
print(F(161,2))