# 1

# (2.) объектно-ориентированное программирование, есть класс
# (3.) функциональное программирование, ссылочно-прозрачная функция
# (1.) императивное программирование, так как используется цикл внутри функций

# 2

def sum_even_numbers(numbers):
    if len(numbers) == 0:
        return 0
    else:
        if numbers[0] % 2 == 0:
            return numbers[0] + sum_even_numbers(numbers[1:])
        else:
            return sum_even_numbers(numbers[1:])


numbers = [14, 93, 19, 38, 18, 51, 77]
print(sum_even_numbers(numbers))
print(numbers)


# 70

# 3

def sum_even_numbers(numbers):
    s = 0
    for i in numbers:
        if i % 2 == 0:
            s += i
    return s


numbers = [60, 84, 9, 49, 7, 85, 38]

print(sum_even_numbers(numbers))

# 182
