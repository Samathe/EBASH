from functools import cache, lru_cache


@lru_cache(None)
def F(x):
    if x <= 1:
        return 1
    else:
        return F(x-1)+F(x-2)

for i in range(100):
    print(i, F(i))