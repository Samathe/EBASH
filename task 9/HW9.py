# 1
# Answer: 77

def summa_a(a):
    s = 0
    for i in a:
        s += i
    return s


print(summa_a([1, 7, 42, 12, 10, 1, 4, 0]))


# 2
# Answer: True

def interval(n, l, r):
    if l <= n <= r:
        return True
    else:
        return False


print(interval(7, 1, 9))


# 3
# Answer: True

def is_perfect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False


print(is_perfect_number(8128))


# 4
# Answer: False

def is_polindrom(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False


print(is_polindrom(1234567899876554321))


# 5
# Answer: False

def find_div(n):
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


print(is_prime(123321))


# 6
# Answer: 34

def F(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)


print(F(10))
