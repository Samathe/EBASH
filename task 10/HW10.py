# 1
# Answer {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

def list_to_dict(a):
    slovar = {}
    for i in a:
        slovar[i] = i
    return slovar


print(list_to_dict([1, 2, 3, 4, 5]))
from string import punctuation


# 2
# Answer {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def gen_dict(n):
    slovar = {}
    for x in range(1, n + 1):
        slovar[x] = x * x
    return slovar


print(gen_dict(5))


# 3
# Answer -165209625

def multiply_items(d):
    m = 1
    for i in d:
        m *= d[i]
    return m


print(multiply_items({'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}))

# 4
# Answer 12

punct = set(".,:;!?")
# print(punct)

text = '''Летний день - это день, когда наступает летнее
солнцестояние и длительность дня достигает своего максимума. В разных странах и
регионах летние дни могут иметь разную продолжительность и характеризоваться
разными погодными условиями. Вообще, летние дни обычно ассоциируются с теплой
и ясной погодой, зелеными лугами, пляжами, купанием в море или озере, пикниками и барбекю. В летние дни люди часто отдыхают и проводят время на открытом
воздухе, занимаются спортом, путешествуют и открывают новые места!'''

c = 0

for i in text:
    if i in punct:
        c += 1
print(c)


# 5
# Answer 12456789

def extract_number(text):
    numbers = "0123456789"
    massive = []
    for i in numbers:
        for j in text:
            if i == j:
                massive.append(j)
                break
    return massive


print(''.join(extract_number("kn1mb9c7c5cv5cc9cvv7cx9sd8nm4cz2bm4k6hf9d")))
