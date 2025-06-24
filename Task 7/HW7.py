# 1
# Answer: 338350

print(sum([i ** 2 for i in range(1, 101)]))

# 2
# Answer: 0 8 16 24 32

# 3
# Answer: 10

print(sum([1 for i in range(2, 21, 2)]))

# 4
# Answer: 3

print(sum([1 for i in list(map(int, input().split()))[::2] if i % 2 == 0]))

# 5
# Answer: 220

print(sum([1 for i in range(1, 1001) if (i % 7 == 0) or (i  % 11 == 0) ]))