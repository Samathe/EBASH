# 1
names = ['Александр', 'Алекс', 'Альберт']

surnames = ['Вотяк', 'Вотяков', 'Вотякович']

patronymics = ['Романович']

for surname in surnames:
    for name in names:
        for patronymic in patronymics:
            print(f'Диплом с отличием вручается {surname}у {name}у {patronymic}у.')

# 2

A = input()
B = int(input())
C = int(input())

print(f"{A}{B:04}-{C:03}")

# 3

a = int(input())
b = int(input())

r = abs(len(str(a)) - len(str(b)))

if a > b:
    print(a)
    print(f'{b:{len(str(b)) + r}}')
    print(a + b)
else:
    print(f'{a:{len(str(a)) + r}}')
    print(b)
    print(a + b)

# 4

r = 1 + int(input()) / 100
k = int(input())

print(f'{100000000 * r ** k:,.2f}')

# 5
for a in range(1, 101):
    for b in range(1, 101):
        result = a * b
        print(result)
        if '0' in str(a * b):
            print(f'[DEBAG] {a=} {b=} {result=}')


# 6


def ip(a, b, c, d):
    print("Восьмибитном двоичном:", ("{:08b}." * 4)[:-1].format(a, b, c, d))
    print("Двоичном:", ("{:b}." * 4)[:-1].format(a, b, c, d))
    print("Восьмиричном:", ("{:x}." * 4)[:-1].format(a, b, c, d))
    print("Десятичном:", ("{}." * 4)[:-1].format(a, b, c, d))
    print("Шестнадцатиричном:", ("{:x}." * 4)[:-1].format(a, b, c, d))


ip(12, 43, 23, 2)
