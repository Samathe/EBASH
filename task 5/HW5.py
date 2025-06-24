#1
#Answer: 3 9 15

n = int(input())
for i in range(n + 1):
    if i % 3 == 0 and i % 6 != 0:
        print(i, end=' ')

#2
#Answer: 10 12 14 16

n = int(input())

for i in range (10, n + 1):
    if i % 2 == 0:
        print(i, end = ' ')


#3
#Answer: 50 2500
n = int(input())
counter = 0
summa = 0
if n % 2 == 0:
    for i in range(1, n + 1):
        if i % 2 == 0:
            counter += 1
    print(counter)
else:
    for i in range(1, n + 1):
        if i % 2 != 0:
            summa += i
    print(summa)

#4
# Answer:8 64 512 4096 32768 262144 2097152 16777216
# 14

n = int(input())
counter = 0
if n % 3 == 0:
    m = int(input())
    for i in range(1, n + 1):
        if i % m == 0:
            counter += 1
    print(counter)
else:
    for i in range(1, n + 1):
        print(n ** i, end=' ')


#5
#Answer: 1 

a = int(input())
b = int(input())
n = int(input())
counter = 0

for i in range(n):
    c = int(input())
    if (c > 10) and (c % 3 == 0 or c % 4 == 0) and (a ** 2 + b ** 2 == c ** 2):
        counter += 1

print(counter)
