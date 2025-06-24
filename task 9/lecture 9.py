"""def find_div(n):
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)
    return a


def is_prime(n):
    if len(find_div(n)) == 2:
        return True
    else:
        return False


k = 0
n = int(input())
for i in range(n):
    if is_prime(i):
        print(' ' * (len(str(n)) - len(str(i)) - 1), i, end=' ', sep = '')
        k += 1
        if k % 10 == 0:
            print()"""


def f(x):
    if x == 0:
        return 0
    if x > 0:
        return f(x-1) + 5

print(f(10))
