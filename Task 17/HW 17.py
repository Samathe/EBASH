# 1
def sum_numbers(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_numbers(1, 2, 3)) # 6
print(sum_numbers(10, 20, 30, 40)) # 100


# 2
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name='Alice', age=25, country='USA')


# 3

def filter_by_length(min_lenght, *list):
    a = []
    for item in list:
        if min_lenght <= len(item):
            a.append(item)
    return a


strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(4, *strings))
# ['hello', 'world']
print(filter_by_length(3, *strings))


# ['hello', 'world', 'how', 'are', 'you']

# 4

def calculate_total_price(price, **discounts):
    total_dis = 0
    for name, value in discounts.items():
        total_dis += value
    return price * (1 - total_dis / 100)


print(calculate_total_price(100, student=10, coupon=20))  # 70.0
print(calculate_total_price(200, holiday=25))  # 150.0
print(calculate_total_price(500))  # 500.0


# 5
def custom_print(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')

    if end != '\n':
        end += '\n'

    output = []
    for arg in args:
        output.append(str(arg))

    for key, value in kwargs.items():
        if key not in ['sep', 'end']:
            output.append(f'{key}={value}')
    print(sep.join(output), end = end)




custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
# 1-2-3-a=4-b=5!
custom_print('Hello', 'World', sep=' ')
# Hello World
custom_print('apple', 'banana', 'cherry', sep=', ')
# apple, banana, cherry
custom_print(a=1, b=2, end='...')
# a=1 b=2...
