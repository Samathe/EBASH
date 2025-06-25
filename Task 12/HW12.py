#1
#Answer:
# 4 1
# 5 6

#2
#Answer:
# П
# П
# Ш


#3
#Answer: bee


#4
#Answer: True False

a = [int(s) for s in range(1, 20)]
iterator = iter(a)
print(9 in iterator)
print(9 in iterator)

#5
#Answer: 1 4 16



#6
#Answer: 1 9 25
a = (n**2 for n in range(1,6))
print(next(a))
next(a)
print(next(a))
next(a)
print(next(a))

#7
#Answer:

creasti_carts = [f"{i} Крести" for i in range(6, 13)]
bubny_carts = [f"{i} бубны" for i in range(6, 13)]
chervi_carts = [f"{i} червы" for i in range(6, 13)]
piki_carts = [f"{i} пики" for i in range(6, 13)]

all_cards = iter(creasti_carts + bubny_carts + chervi_carts + piki_carts)

print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
print(next(all_cards))
