# 1
# Answer : 108

# 2
# Answer :

import copy

a = []
for i in range(5):
    a.append(int(input()))

b = a[:]
c = a.copy()
d = copy.copy(a)
e = copy.deepcopy(a)
f = list(a)

print(5, sum(a))

# 3
# Answer : 966

# 4
# Answer : 36 12884901885
import sys

s = 0
animals = ["cat", "cat", "dog", "dog", "bird", "capybara", "capybara", "capybara"]
count_animals = {}
for animal in set(animals):
    count_animals[animal] = 0
for animal in set(animals):
    for i in range(len(animals)):
        if animal == animals[i]:
            count_animals[animal] += 1

for animal in set(animals):
    s += sys.getrefcount(animal)

print(s, sys.getrefcount(1) + sys.getrefcount(2) + sys.getrefcount(3))
print(count_animals)
# 5
# Answer : 15 21
backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara", 2999, 2999, "capybara", [7, 7, 7], [7, 7, 7],
            [7, 7, 7], [7, 7, 7]] + [[8, 8]] * 5
count_is = 0
count_eq = 0
for i in range(1, len(backpack)):
    for j in range(0, i):
        if backpack[i] is backpack[j]:
            count_is += 1
        if backpack[i] == backpack[j]:
            count_eq += 1
print(count_is, count_eq)
# 6
# Answer :


salat = []

salat.append("lettuce")
salat.append("chicken")
salat.append("cheese")
salat.append("sauce")
salat.append("tomatoes")
salat.append("croutons")
salat.append(salat)

# print(salat)

salat.append("salt")
# print(salat)
salat.append("pepper")
# print(salat)

print(salat[4], salat[-1])
