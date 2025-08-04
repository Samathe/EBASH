# ООП. Dunder или магические методы
## Задача 1
'''
После отправки очередного письма в деканат, студента Пётра Васильева
пробила ностальгия, и он вспоминил, как однажды в 2007-м подключил ко
всем сообщениям себе на телефоне очень крутую подпись:
* `-~=$([{PETR}])$=~-`
Сейчас Пётр участвует в соревновании CTF "Крутые хакеры 2023" и хочет
разработать прототип вируса, который бы заставлял всех оппонентов
заразиться ностальгией, чтобы они потеряли время и команда Петра смогла
бы "захватить" все флаги. Пётр решил обфусцировать свой код, поэтому
реализует такой вирус с помощью перегрузки магических методов.
Реализуйте класс `SignedMessage`, который бы обладал следующими
характеристиками:
* Класс инициализируется (`__init__`) с помощью `SignedMessage(message,
signature)`, где `message` -- сообщение, представленное строкой, а
`signature` -- очень крутая подпись.
* Репрезентация класса в виде строки выглядит как `"{message}
{signature}"`. Пётр хочет всех обмануть, и добавлять очень крутую подпись
после каждого вызова `str()` (используйте перегрузку магического метода
`__str__`).
* Чтобы вирус дольше не был обнаружен, нужно реализовать операцию
строкового сложения. При сложении двух сообщений в одно, подпись не
должна оставаться после каждого сообщения, а находиться только лишь в
конце. Для этого стоит перегрузить метод `__add__`.
* Подумав, Пётр решил добавить дополнительный функционал вирусу: при
создании нового объекта класса он собирается вызывать функцию
`infiltrate()`. Об этой функции никто не должен знать, потому что Пётр
хочет использовать её для своих злостных целей после того, как вирус
распространится. Реализуйте вызов этой функции при создании нового
объекта `SignedMessage`, ничего больше не меняя в методе `__new__`.
```python
def infiltrate():
 # здесь Пётр позже напишет код
 pass
```
Пример использования сложения классов `SignedMessage`:
```python
SIGNATURE = "-~=$([{PETR}])$=~-"
# выводится "Hello -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE))
# выводится "world! -~=$([{PETR}])$=~-"
print(SignedMessage("world!", SIGNATURE))
# выводится "Hello world! -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world!",
SIGNATURE))
'''


class SignedMessage:
    def __new__(cls, *args, **kwargs):
        # Call infiltrate() when creating new object
        def infiltrate():
            # здесь Пётр позже напишет код
            pass

        infiltrate()
        return object.__new__(cls)

    def __init__(self, message, signature):
        self.message = message
        self.signature = signature

    def __str__(self):
        # Format: "{message} {signature}"
        return f"{self.message} {self.signature}"

    def __add__(self, other):
        # Combine messages, keep signature only at the end
        # Return new SignedMessage object, not string
        combined_message = self.message + other.message
        return SignedMessage(combined_message, self.signature)


# Test code
SIGNATURE = "-~=$([{PETR}])$=~-"

# Test individual messages
msg1 = SignedMessage("Hello ", SIGNATURE)
print(msg1)  # Should print: "Hello -~=$([{PETR}])$=~-"

msg2 = SignedMessage("world!", SIGNATURE)
print(msg2)  # Should print: "world! -~=$([{PETR}])$=~-"

# Test addition
combined = msg1 + msg2
print(combined)  # Should print: "Hello world! -~=$([{PETR}])$=~-"

"""
## Задача 2
**Векторы** — это очень важный концепт во многих сферах науки, связанных
с математикой: математическом анализе, линейной алгебре и физике.
Очевидно, что они также являются очень важной частью компьютерных наук и
используются повсеместно, например, в геймдеве.
Вам не понравилась встроенная реализация вектора в библиотеке, которую вы
установили, поэтому вы решили написать свою реализацию.
Реализуйте классы `Vector2` для двухмерного вектора и `Vector3` для
трёхмерного вектора.
***Подсказка:** мы хотим, чтобы вы реализовали класс векторов, с которым
удобно выполнять математические операции. В Python двухмерным вектором
можно назвать список формата `[x, y]`, а трёхмерным — `[x, y, z]`.*
Класс `Vector3` инициализируется (`__init__`) как `Vector3(x, y, z)`, где
`x`, `y`, `z` — соответствующие координаты по осям `x`, `y` и `z`:
```python
class Vector3:
 def __init__(self, x, y, z):
 self.x = x
 self.y = y
 self.z = z
```
Перегрузите следующие магические методы для классов `Vector2` и `Vector3`
(описания методов показаны на примере трёхмерного вектора):
* `__add__` — сложение векторов;
 * `Vector3(1, 2, 3) + Vector3(3, 4, 5) == Vector3(4, 6, 8)`;
* `__neg__` — отражение вектора;
 * `-Vector3(1, 0, -1) == Vector3(-1, 0, 1)`;
* `__sub__` — вычитание векторов;
 * `Vector3(7, 7, 7) - Vector3(3, 2, 1) == Vector3(4, 5, 6)`;
* `__abs__` — нахождение длины (абсолютного значения) вектора;
 * `abs(Vector3(3, 4, 0)) == len(Vector3(3, 4, 0)) == 5`;
* `__str__` — репрезентация вектора в виде строки формата `{0, 5, 2}`;
 * `str(Vector3(0, 5, 2)) == "{0, 5, 2}"`
 * можно придумать свою репрезентацию;
* `__eq__` — операция `==` для двух векторов;
* `__ne__` — операция `!=` для двух векторов;
* `__mul__` — операция скалярного произведения.
> Скалярное произведение двух трёхмерных векторов находится по следующей
формуле:

> Реализация двухмерного вектора аналогична реализации трёхмерного
вектора, но принимает на вход два аргумента, которые описывают координаты
`x` и `y`.
"""
print("-" * 100)

import math


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return math.sqrt(sum([math.pow(self.x, 2), math.pow(self.y, 2)]))

    def __len__(self):
        return int(math.sqrt(sum([math.pow(self.x, 2), math.pow(self.y, 2)])))

    def __str__(self):
        return f"|{self.x}|\n|{self.y}|"

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return (self.x != other.x or self.y != other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * self.y


V1 = Vector2(1, 2)
V2 = Vector2(-1, 2)

V3 = V1 + V2
print(V3.x, V3.y)
V4 = -V1
print(V4.x, V4.y)
V5 = V1 - V2
print("V1 - V2 = ", V5.x, V5.y)
print(len(V1))
print(abs(V1))
print(str(V3))


class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return math.sqrt(sum([math.pow(self.x, 2), math.pow(self.y, 2), math.pow(self.z, 2)]))

    def __len__(self):
        return int(math.sqrt(sum([math.pow(self.x, 2), math.pow(self.y, 2), math.pow(self.z, 2)])))

    def __str__(self):
        return f"|{self.x}|\n|{self.y}|\n|{self.z}|"

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __ne__(self, other):
        return (self.x != other.x or self.y != other.y or self.z != other.z )

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


# Test the implementation
print("=" * 50)
print("TESTING VECTOR2")
print("=" * 50)

V1 = Vector2(1, 2)
V2 = Vector2(-1, 2)
print(f"V1 = {V1}")  # {1, 2}
print(f"V2 = {V2}")  # {-1, 2}

# Addition
V3 = V1 + V2
print(f"V1 + V2 = {V3}")  # {0, 4}

# Negation
V4 = -V1
print(f"-V1 = {V4}")  # {-1, -2}

# Subtraction
V5 = V1 - V2
print(f"V1 - V2 = {V5}")  # {2, 0}

# Absolute value (length)
print(f"abs(V1) = {abs(V1):.3f}")  # 2.236 (sqrt(5))

# Dot product
print(f"V1 * V2 = {V1 * V2}")  # 3 (1*(-1) + 2*2 = -1 + 4 = 3)

# Equality
print(f"V1 == V2: {V1 == V2}")  # False
print(f"V1 != V2: {V1 != V2}")  # True

print("\n" + "=" * 50)
print("TESTING VECTOR3")
print("=" * 50)

# Create test vectors
V6 = Vector3(1, 2, 3)
V7 = Vector3(3, 4, 5)
print(f"V6 = {V6}")  # {1, 2, 3}
print(f"V7 = {V7}")  # {3, 4, 5}

# Addition - example from task
V8 = V6 + V7
print(f"V6 + V7 = {V8}")  # {4, 6, 8}
print(f"Vector3(1, 2, 3) + Vector3(3, 4, 5) == Vector3(4, 6, 8): {V8.x == 4 and V8.y == 6 and V8.z == 8}")

# Negation - example from task
V9 = -Vector3(1, 0, -1)
print(f"-Vector3(1, 0, -1) = {V9}")  # {-1, 0, 1}
print(f"-Vector3(1, 0, -1) == Vector3(-1, 0, 1): {V9.x == -1 and V9.y == 0 and V9.z == 1}")

# Subtraction - example from task
V10 = Vector3(7, 7, 7) - Vector3(3, 2, 1)
print(f"Vector3(7, 7, 7) - Vector3(3, 2, 1) = {V10}")  # {4, 5, 6}
print(f"Vector3(7, 7, 7) - Vector3(3, 2, 1) == Vector3(4, 5, 6): {V10.x == 4 and V10.y == 5 and V10.z == 6}")

# Absolute value - example from task
abs_result = abs(Vector3(3, 4, 0))
print(f"abs(Vector3(3, 4, 0)) = {abs_result}")  # 5.0
print(f"abs(Vector3(3, 4, 0)) == 5: {abs_result == 5}")

# String representation - example from task
str_vector = Vector3(0, 5, 2)
print(f'str(Vector3(0, 5, 2)) = "{str_vector}"')  # "{0, 5, 2}"
print(f'str(Vector3(0, 5, 2)) == "{{0, 5, 2}}": {str(str_vector) == "{0, 5, 2}"}')

# Dot product examples
dot_product = V6 * V7
print(f"V6 * V7 = {dot_product}")  # 26 (1*3 + 2*4 + 3*5 = 3 + 8 + 15 = 26)

# More dot product examples
zero_vector = Vector3(0, 0, 0)
unit_x = Vector3(1, 0, 0)
unit_y = Vector3(0, 1, 0)
unit_z = Vector3(0, 0, 1)

print(f"unit_x * unit_y = {unit_x * unit_y}")  # 0 (perpendicular vectors)
print(f"unit_x * unit_x = {unit_x * unit_x}")  # 1 (unit vector with itself)

# Equality tests
equal_vector = Vector3(1, 2, 3)
print(f"V6 == Vector3(1, 2, 3): {V6 == equal_vector}")  # True
print(f"V6 == V7: {V6 == V7}")  # False
print(f"V6 != V7: {V6 != V7}")  # True

print("\n" + "=" * 50)
print("ADDITIONAL PRACTICAL EXAMPLES")
print("=" * 50)

# Physics example: displacement vectors
position1 = Vector3(10, 5, 0)  # Starting position
displacement = Vector3(-3, 2, 1)  # Movement vector
position2 = position1 + displacement  # Final position
print(f"Position1: {position1}")
print(f"Displacement: {displacement}")
print(f"Position2: {position2}")  # {7, 7, 1}

# Distance calculation
distance = abs(displacement)
print(f"Distance traveled: {distance:.3f}")

# Force vectors example
force1 = Vector3(10, 0, 0)  # Force in x direction
force2 = Vector3(0, 15, 0)  # Force in y direction
resultant_force = force1 + force2
print(f"Force1: {force1}")
print(f"Force2: {force2}")
print(f"Resultant force: {resultant_force}")
print(f"Magnitude of resultant force: {abs(resultant_force):.3f}")

# Work calculation (force dot displacement)
work = force1 * Vector3(5, 0, 0)  # Force in x, displacement in x
print(f"Work done by force1 over displacement (5,0,0): {work}")  # 50 units
"""
## Задача 3
Начинающая разработчица Анна решила создать свою игру-песочницу.
Вдохновляясь своим десятилетним опытом игры в Майнкрафт, она начала
задумываться, чего ей не  ватало всё это время.
Первое, что пришло ей в голову — автоматическая сортировка инвентаря,
поэтому Анна решила реализовать её в своей игре.
На данный момент класс предмета `Item` выглядит следующим образом:
```python
class Item:
 def __init__(self, ID, price, rarity, color):
 self.ID = ID
 self.price = price
 self.rarity = rarity
 self.color = color
new_item = Item(128, 500, 1, "FF5819")
```
У класса есть параметры, заданные следующими типами данных:
* `ID` -- идентификатор предмета, неотрицательное целочисленное значение;
* `price` -- цена предмета, неотрицательное целочисленное значение;
* `rarity` -- "редкость" предмета, где:
 * `0` -- обычный;
 * `1` -- редкий;
 * `2` -- эпический;
 * `3` -- легендарный;
 * можно использовать библиотеку
[enum](https://docs.python.org/3/library/enum.html);
* `color` -- цвет предмета в hex-записи (шестнадцатиричное число),
хранится в виде строки;
 * Типовой формат: `FF5819`
Чтобы сортировка правильно работала везде, Анне требуется перегрузить
магические методы для операторов:
* `<` (`__lt__`);
* `<=` (`__le__`);
* `>` (`__gt__`);
* `>=` (`__ge__`);
* `!=` (`__ne__`);
* `==` (`__eq__`).
> Если писать код напрямую, то его большая часть для перегрузок
операторов сравнения будет одинаковой. Подумайте, как это эффективно
написать и избежать повторения кода.
Анна придумала следующий порядок сортировки, потому что ей показалось,
что так будет удобнее всего:
* Сначала предметы сортируются в порядке **возрастания** по `ID`.
* Если `ID` одинаковые, то предметы располагаются по **возрастанию** по
`price`.
* Если `price` одинаковая, то предметы располагаются по **убыванию** по
`rarity` (легендарные предметы должны идти раньше обычных).
* Если `rarity` одинаковая, то предметы располагаются по цвету от самого
светлого цвета до самого тёмного по **убыванию** насыщенности сначала по
красному, потом по зелёному, а затем по синему цвету.
 * В hex-кодировке цветов первые два символа кодируют красный цвет,
затем следующие два — зелёный и последние два — синий. **Это позволяет
просто расположить строки цветов по убыванию**, чтобы добиться
результата, который описывается в алгоритме.
Вы можете реализовать приоритет сортировки, придуманный Анной, или
придумать свой (обязательно оставьте об этом комментарии, где будет
описано, почему вы решить сделать по-другому).
Реализуйте функционал, описанный выше, создайте список предметов и
примените к нему метод `.sort()`, чтобы удостовериться, что вы всё
реализовали правильно.
"""
from enum import Enum
from functools import total_ordering


class Rarity(Enum):
    """Перечисление для редкости предметов"""
    COMMON = 0  # обычный
    RARE = 1  # редкий
    EPIC = 2  # эпический
    LEGENDARY = 3  # легендарный


@total_ordering
class Item:
    """
    Класс предмета с автоматической сортировкой по следующим критериям:
    1. ID (по возрастанию)
    2. price (по возрастанию)
    3. rarity (по убыванию - легендарные первыми)
    4. color (по убыванию hex-значения - от светлого к темному)
    """

    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        # Поддерживаем как enum, так и int для rarity
        if isinstance(rarity, int):
            self.rarity = Rarity(rarity)
        else:
            self.rarity = rarity
        self.color = color

    def _comparison_key(self):
        """
        Возвращает кортеж для сравнения объектов.
        Используется отрицательное значение rarity для сортировки по убыванию.
        Цвет сортируется по убыванию (от FF до 00).
        """
        return (
            self.ID,  # по возрастанию
            self.price,  # по возрастанию
            -self.rarity.value,  # по убыванию (инвертируем знак)
            self.color[::-1]  # по убыванию hex (обращаем строку)
        )

    def __eq__(self, other):
        """Проверка равенства предметов"""
        if not isinstance(other, Item):
            return NotImplemented
        return self._comparison_key() == other._comparison_key()

    def __lt__(self, other):
        """Проверка "меньше чем" для сортировки"""
        if not isinstance(other, Item):
            return NotImplemented
        return self._comparison_key() < other._comparison_key()

    def __repr__(self):
        """Строковое представление предмета для удобства отладки"""
        rarity_names = {0: "Common", 1: "Rare", 2: "Epic", 3: "Legendary"}
        return (f"Item(ID={self.ID}, price={self.price}, "
                f"rarity={rarity_names[self.rarity.value]}, color=#{self.color})")


# Создаем список предметов для тестирования
def create_test_items():
    """Создает список тестовых предметов"""
    items = [
        Item(128, 500, 1, "FF5819"),  # Rare, красно-оранжевый
        Item(100, 300, 3, "000000"),  # Legendary, черный
        Item(128, 500, 2, "FF5819"),  # Epic, красно-оранжевый (тот же цвет)
        Item(100, 300, 0, "FFFFFF"),  # Common, белый
        Item(200, 150, 1, "00FF00"),  # Rare, зеленый
        Item(128, 600, 1, "FF5819"),  # Rare, красно-оранжевый (другая цена)
        Item(100, 300, 3, "FFFFFF"),  # Legendary, белый
        Item(128, 500, 1, "0000FF"),  # Rare, синий
    ]
    return items


# Демонстрация работы
if __name__ == "__main__":
    print("=== Демонстрация автоматической сортировки инвентаря ===\n")

    # Создаем список предметов
    items = create_test_items()

    print("Исходный список предметов:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

    # Сортируем список
    items.sort()

    print("\nОтсортированный список предметов:")
    print("(ID↑, price↑, rarity↓, color↓)")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

    print("\n=== Тестирование операторов сравнения ===")

    item1 = Item(100, 500, 1, "FF0000")
    item2 = Item(100, 500, 2, "FF0000")  # Более высокая редкость
    item3 = Item(100, 500, 1, "FF0000")  # Идентичный item1

    print(f"item1: {item1}")
    print(f"item2: {item2}")
    print(f"item3: {item3}")
    print()

    print(f"item1 == item3: {item1 == item3}")  # True
    print(f"item1 == item2: {item1 == item2}")  # False
    print(f"item1 < item2: {item1 < item2}")  # True (меньшая редкость)
    print(f"item2 > item1: {item2 > item1}")  # True
    print(f"item1 != item2: {item1 != item2}")  # True
    print(f"item1 <= item3: {item1 <= item3}")  # True
    print(f"item1 >= item3: {item1 >= item3}")  # True

    print("\n=== Проверка сортировки по цвету ===")
    color_items = [
        Item(1, 100, 1, "FFFFFF"),  # Белый (самый светлый)
        Item(1, 100, 1, "FF0000"),  # Красный
        Item(1, 100, 1, "00FF00"),  # Зеленый
        Item(1, 100, 1, "0000FF"),  # Синий
        Item(1, 100, 1, "000000"),  # Черный (самый темный)
    ]

    print("Цвета до сортировки:")
    for item in color_items:
        print(f"  #{item.color}")

    color_items.sort()

    print("Цвета после сортировки (от светлого к темному):")
    for item in color_items:
        print(f"  #{item.color}")
