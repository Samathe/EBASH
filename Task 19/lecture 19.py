def kvadrator(func):
    def g(x):
        return (func(x))**2
    return g
@kvadrator
def f(x):
    return x+2

print(f(10))

def my_decorator(func):
    def inside_func():
        print('Gello')
        func()
        print("Fine")
    return inside_func

def doubler(func):
    def inside_func():
        func()
        func()
    return inside_func


@my_decorator
@doubler
def f():
    print("Helli")

f()

def my_cacher(func):
    D = dict()
    def inside_func(x):
        if x not in D:
            D[x] = func(x)
        return D[x]
    return inside_func

@my_cacher
def f(x):
    if x<=1:
        return 1
    else:
        return f(x-1)+ f(x-2)

for i in range(100):
    print(f(i))

import time
def timer(func):
    def inside_func(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        fin = time.time()
        print(f'Function {func.__name__} works {fin-st}')
        return  result
    return inside_func
@timer
def f(x):
    k = 0
    for i in range(x):
        for j in range(x):
            if (i + j) % 100 == 0:
                k += 1

    print(k)
f(1000)
f(2000)
f(4000)