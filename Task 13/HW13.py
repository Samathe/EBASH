# 1
# Answer : ['Женя', 'Вася']

# 2
# Answer : [8, 64, 216, 512, 1000]

cube = lambda List: list(map(lambda x: x ** 3, List))

print(cube([2, 4, 6, 8, 10]))

# 3
# Answer : [-1, -7, -8, -10]

negative = lambda List: list(filter(lambda x: x < 0, List))
print(negative([-1, 4, -7, -8, -10, 1, 0]))
# 4
# Answer : 40320

import functools

n = int(input())
factorial = lambda x: int(functools.reduce(lambda x, y: x * y, range(1, x + 2)) / (x + 1))
print(factorial(n))

# 5
# Answer : 6

import functools

maximum = lambda x, y: (x > y) * x + (y > x) * y
# print(maximum(1,4))
# print(maximum_in_list)

kraten_9 = lambda List: list(filter(lambda x: (x ** 2) % 9 == 0, List))

maximum_in_list = lambda List: functools.reduce(maximum, kraten_9(List))

print(maximum_in_list([2, 4, 6, 8, 0, 3, 4, 2, 3, 5, 1, 2]))
