# 1
def f(a):
    return a * b * 18

print(f(1))
# Answer: NameError: name 'b' is not defined

# 2
"summa = 0

for i in range(1, 11):
    summa += i
print(summa)

# NameError: name 'summa' is not defined)

# 3
def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")

is_even("4")

# TypeError: not all arguments converted during string formatting

# 4
def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


# 5
def is_palindrom(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

print(is_palindrom("ABCDCBA"))

# 6
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in lst:
            result = result * i
        return result

print(multiplylist([1,4,5]))