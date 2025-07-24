# Функциональное программирование. Домашнее задание
## Задача 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(100))


## Задача 2

def devisions(n, List=[], i=0):
    new_List = List
    new_i = i + 1
    if i == n:
        return List
    else:
        if n % new_i == 0:
            new_List.append(new_i)
        return devisions(n, new_List, new_i)


def is_prime(n):
    if len(devisions(n)) == 2:
        return True
    else:
        return False


print(is_prime(101))

"""
## Задача 3
Напишите функцию `filter_odd`, которая принимает список целых чисел и
возвращает новый список, содержащий только нечетные числа.
#### Входные аргументы:
- `numbers` — список целых чисел.
#### Возвращаемое значение:
- Новый список, содержащий только нечетные числа из исходного списка.
#### Примечания:
- Для решения задачи используйте функцию `filter` и `lambda`-функцию.
"""
filter_odd = lambda List: list(filter(lambda x: x % 2 == 1, List))

print(filter_odd([1, 2, 3, 4]))

"""
## Задача 4
Напишите функцию `map_square`, которая принимает список чисел и
возвращает новый список, содержащий квадраты этих чисел.
#### Входные аргументы:
- `numbers` — список чисел.
#### Возвращаемое значение:
- Новый список, содержащий квадраты чисел из исходного списка.
#### Примечания:
- Для решения задачи используйте функцию `map` и `lambda`-функцию

"""

map_square = lambda List: list(map(lambda x: x ** 2, List))
L1 = [1, 2, 3, 4]
print(map_square(L1))
"""
## Задача 5
Напишите функцию `reduce_sum`, которая принимает список чисел и
возвращает сумму этих чисел.
#### Входные аргументы:
- `numbers` — список чисел.
#### Возвращаемое значение:
- Сумма чисел из исходного списка.
#### Примечания:
- Для решения задачи используйте функцию `reduce` из модуля `functools` и
`lambda`-функцию.
"""

from functools import reduce

reduce_sum = lambda List: reduce(lambda x, y: x + y, List)

print(reduce_sum(L1))

"""
## Задача 6
Напишите функцию `partial_apply`, которая принимает на вход функцию
`func` с двумя аргументами и возвращает новую функцию `partial_func`,
которая является частичным применением первоначальной функции `func` с
одним аргументом.
#### Описание:
Частичное применение функции — это процесс создания новой функции с
фиксированными значениями некоторых из начальных аргументов. Новая
функция принимает только оставшиеся аргументы и выполняет вычисления на
основе исходной функции.
#### Входные аргументы:
- `func` — функция, которую необходимо частично применить.
#### Возвращаемое значение:
- Новая функция `partial_func`, которая является частичным применением
функции `func` и принимает только один аргумент.
#### Примечания:
- Для решения задачи используйте возможности функционального
программирования в Python, такие как замыкания и `lambda`-функции.
"""


def partial_apply(func):
    print(f"В partial_apply: func = {func}")

    def partial_func(x):
        print(f"В partial_func: x = {x}, func = {func}")  # func из внешней области!

        return lambda y: func(x, y)  # x и func захвачены замыканием

    return partial_func


f = lambda x, y: x + y
partial_f = partial_apply(f)  # func "захвачена"
add_5 = partial_f(5)  # x=5 "захвачена"
result = add_5(3)  # Использует захваченные func и x=5
print(result)  # 8
"""
## Задача 7
Напишите функцию `compose`, которая принимает на вход две функции `f` и
`g` и возвращает новую функцию `h`, которая является композицией этих
двух функций.
#### Описание:
Композиция функций — это процесс создания новой функции путем
последовательного применения одной функции к результату другой функции.
#### Входные аргументы:
- `f` — первая функция, которая применяется к аргументу.
- `g` — вторая функция, которая применяется к результату функции `f`.
#### Возвращаемое значение:
- Новая функция `h`, которая является композицией функций `f` и `g`.
#### Примечания:
- Для решения задачи используйте возможности функционального
программирования в Python, такие как замыкания и `lambda`-функции.
"""


def compose(f, g):
    def h(x):
        return f(g(x))

    return h


compose1 = compose(lambda x: x ** 2, lambda x: x + 1)
compose2 = compose(lambda x: x + 1, lambda x: x ** 2)

print(compose1(3), compose2(3))
"""
## Задача 8
Напишите функцию `create_function_with_arguments`, которая принимает на
вход функцию `func` и список `arguments`, и возвращает новую функцию
`new_func`. При вызове `new_func` она вызывает `func` с переданными
аргументами `arguments` и возвращает результат.
#### Входные аргументы:
- `func` — исходная функция, которая должна быть вызвана.
- `arguments` — список аргументов, которые должны быть переданы в функцию
`func`.
#### Возвращаемое значение:
- Функция `new_func`, которая вызывает `func` с переданными аргументами
`arguments` и возвращает результат.

"""


def create_function_with_arguments(func, arguments):
    def new_func():
        return func(*arguments)

    return new_func


my_func = create_function_with_arguments(lambda x: x ** 2, [5])

print(my_func())  # 25

print(my_func)  # <function...> - это объект функции

"""

## Задача 9
Напишите функцию `compose_functions`, которая принимает список функций
`functions` и возвращает новую функцию `composed_function`. При вызове
`composed_function` она последовательно применяет все функции из списка
`functions` к переданному аргументу и возвращает результат.
#### Входные аргументы:
- `functions` — список функций, которые должны быть применены к
аргументу.
#### Возвращаемое значение:
- Функция `composed_function`, которая последовательно применяет все
функции из списка `functions` к переданному аргументу и возвращает
результат."""


def compose_functions(functions):

    def composed_function(x, index = 0):
        if index + 1 == len(functions):
            return x
        else:
            new_index = index + 1
            return composed_function(functions[new_index](x), new_index)
    return composed_function
f1 = lambda x: x**2
f2 = lambda x: x*4
f3 = lambda x: x%5
f4 = lambda x: x * 8
com = compose_functions([f1,f2,f3,f4, lambda x: x+5])
print(com(11))

