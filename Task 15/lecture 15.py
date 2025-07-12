def f(x, y):
    a = (x ** 2 + y ** 2)
    b = (x + y) ** 2
    return a / b


s = 0

for y in range(-1, 10):
    x = int(input())
    s += f(x, y)
    print(s)
