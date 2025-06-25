"""
a = list(filter(lambda x: x%2 == 0, [12,213, 3,1 ,2]))
print(a)
"""
"""
Print = lambda List: list(map(lambda x: print(x, end = ' '), List))

a = [12, 'Hello', 'Salem']
h = lambda n: (n%2 == 0) * 3 + n%2 - n**(n%3 == 1 * 10)
b = [x**2 + h(x) for x in range(1,20)]
Print(b)
Print(a)"""



"""def apl(func, List):
    last = List[0]
    for x in List[1:]:
        last = func(last, x)
    return last"""

apl = lambda func, List: list(map(func, List))

print(apl(lambda x: x**2, [1,2,3,4]))
