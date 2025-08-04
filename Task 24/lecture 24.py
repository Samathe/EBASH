class Dot:
    DOT_MIN = -1000
    DOT_MAX = 1000

    def __new__(cls, *args, **kwargs):
        print("NEW")
        return object.__new__(cls)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("INIT")


dot = Dot(1, 2)
print(dot)
print("-" * 50)


class Dog:
    element = None

    def __new__(cls, *args, **kwargs):
        if not cls.element:
            cls.element = object.__new__(cls)
            cls.element.initialized = False
            print("Created")
        else:
            print("Error")
        return cls.element

    def __init__(self, name):
        if not self.initialized:
            self.name = name
            print("INIT", name)
            self.initialized = True


d = Dog("Rex")
p = Dog("Pikachu")

print(d)
print(p)

print(d.name)
print(p.name)
# SINGLETON
print("-" * 50)


class Myvector:
    def __init__(self, *args):
        self.coords = args

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return tuple(map(abs, self.coords))

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors have different length")
        L1 = []
        for i in range(len(self)):
            L1.append(self.coords[i] + other.coords[i])
        return Myvector(*L1)

    def __mul__(self, other):
        """if len(self) != len(other):
            raise ValueError("Vectors have different length")
        L1 = []
        for i in range(len(self)):
            L1.append(self.coords[i] * other.coords[i])
        return sum(L1)"""
        if not isinstance(other, int):
            raise ValueError("We can multiply only to scalar")
        L2 = tuple(map(lambda x: x * other, self.coords))
        return Myvector(*L2)

    def __imul__(self, other):
        if not isinstance(other, int):
            raise ValueError("We can multiply only to scalar")
        L2 = tuple(map(lambda x: x * other, self.coords))
        return Myvector(*L2)
    def __getattribute__(self, item):
        print("Call getattribute")
        return object.__getattribute__(self, item)

a = Myvector(10, -2, 4)
b = Myvector(0, -2, 10)

q = a + b
print(q.coords)
k = q * 5
print(k.coords)
k *= 2
print(k.coords)
print("-" * 50)
