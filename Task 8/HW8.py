# 1
# Answer:

for i in range(1, 11):
    for j in range(1, 11):
        if i * j // 10 == 0:
            print('', i * j, end='  ')
        elif i * j // 10 < 10:
            print('', i * j, end=' ')
        else:
            print(i * j, end='')
    print()

# 2
# Answer: 26

l = int(input())
r = int(input())
c = 0
for x in range(l, r + 1):
    for y in range(l, r + 1):
        for k in range(l, r + 1):
            if x ** 2 + y ** 2 == k ** 2:
                c += 1
print(c)
# 3
# Answer: 220 284

N = int(input())

for i in range(2, N):
    for j in range(i + 1, N + 1):
        del_i = [x for x in range(1, i) if i % x == 0]
        del_j = [x for x in range(1, j) if j % x == 0]
        if sum(del_i) == j and sum(del_j) == i:
            print(i, j)

# 4
# Answer: 1634 8208 9474

n = int(input())

for i in range(10 ** (n - 1), 10 ** (n)):
    armstrong = 0
    for j in str(i):
        armstrong += int(j) ** n

    if armstrong == i:
        print(i, end=' ')
