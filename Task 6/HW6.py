# 1
# Answer: [12, 34] 46

a = []
n = int(input())
m = int(input())

a.append(n)
a.append(m)

print(a, sum(a))
# 2
# Answer: Программирование школы

text = input()
a = []
j = 0
for i in range(len(text)):
    if text[i] == ' ':
        a.append(text[j:i])
        j = i + 1
a.append(text[j:-1] + text[-1])

print(a[0], a[-1])

# 3
# Answer: нетипичный

text = input()
a = []
j = 0
for i in range(len(text)):
    if text[i] == ' ':
        a.append(text[j:i])
        j = i + 1
a.append(text[j:-1] + text[-1])
max_len = 0
for i in range(len(a)):
    if max_len < len(a[i]):
        max_len = len(a[i])
        max_word = a[i]
print(max_word)


# 4
# Answer: 234168

n = int(input())
a = []
for i in range(1, n + 1):
    if i % 3 ==  0 or i % 5 == 0:
        a.append(i)
print(sum(a))

# 5
# Answer: cat

text = input()
a = []
j = 0
for i in range(len(text)):
    if text[i] == ' ':
        a.append(text[j:i])
        j = i + 1
a.append(text[j:-1] + text[-1])

uni_a = set(a)
counter = 0
for i in uni_a:
    old_counter = counter
    counter = 0
    for j in range(len(a)):
        if i == a[j]:
            counter += 1
    if counter > old_counter:
        max_counter = counter
        max_word = i

print(max_word)

