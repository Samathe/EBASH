"""# ООП. Классы, атрибуты и методы
## Задача 1
Напишите класс `CoffeeMachine`, который будет иметь следующие атрибуты и
методы:
- `water_level` — уровень воды в кофейном автомате;
- `coffee_level` — уровень кофе в кофейном автомате;
- `milk_level` — уровень молока в кофейном автомате;
- `sugar_level` — уровень сахара в кофейном автомате;
- `cups` — количество доступных чашек для приготовления кофе;
- `__init__(self, water_level, coffee_level, milk_level, sugar_level=0,
cups=0)` — конструктор класса, принимает значения и инициализирует
соответствующие атрибуты;
- `add_water(self, amount)` — метод, который принимает значение
`amount` (количество добавляемой воды) и увеличивает атрибут
`water_level` на это значение;
- `add_coffee(self, amount)` — метод, который принимает значение
`amount` (количество добавляемого кофе) и увеличивает атрибут
`coffee_level` на это значение;
- `add_milk(self, amount)` — метод, который принимает значение `amount`
(количество добавляемого молока) и увеличивает атрибут `milk_level` на
это значение;
- `add_sugar(self, amount)` — метод, который принимает значение
`amount` (количество добавляемого сахара) и увеличивает атрибут
`sugar_level` на это значение;
- `add_cups(self, number)` — метод, который принимает значение `number`
(количество добавляемых чашек) и увеличивает атрибут `cups` на это
значение;
- `check_resources(self)` — метод, который проверяет наличие
достаточных ресурсов (воды, кофе, молока, сахара и чашек) для
приготовления кофе. Если все необходимые ингредиенты и чашки доступны в
достаточном количестве, метод возвращает `True`, иначе возвращает
`False`;
- `make_coffee(self)` — метод, который вызывает метод
`check_resources()` для проверки ресурсов. Если ресурсы доступны, метод
уменьшает уровень ингредиентов на соответствующие значения, уменьшает
количество доступных чашек на $1$ и выводит сообщение «Кофе готов!». Если
ресурсы недостаточны, метод выводит сообщение «Недостаточно
ингредиентов!».

"""


class CoffeeMachine:
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, number):
        self.cups += number

    def check_resources(self):
        return self.water_level >= 200 and self.coffee_level >= 100 and self.milk_level >= 100 and self.sugar_level >= 20 and self.cups >= 10

    def reduce_resources(self):
        self.coffee_level -= 1
        self.sugar_level -= 1
        self.milk_level -= 1
        self.water_level -= 1
        self.cups -= 1

    def make_coffee(self):
        if self.check_resources():
            self.reduce_resources()
            print("Кофе готов!")
        else:
            print("Недостаточно ингредиентов!")

    def show_ingredients(self):
        print(self.__dict__)


Machine = CoffeeMachine(12, 12, 3, 4, 6)

Machine.make_coffee()

Machine.add_water(90)
Machine.add_coffee(90)
Machine.add_milk(90)
Machine.add_cups(10)
Machine.add_sugar(100)

Machine.make_coffee()

Machine.show_ingredients()

Machine.add_milk(7)

Machine.make_coffee()

Machine.add_water(100)
Machine.make_coffee()

"""
## Задача 2
Напишите класс `PhotoCamera`, представляющий простую фотокамеру. Класс
должен иметь следующие атрибуты и методы:
- `brand` — марка фотокамеры;
- `model` — модель фотокамеры;
- `resolution` — разрешение фотографий, где первое число представляет
ширину, а второе — высоту;
- `is_on` — указывает, включена ли фотокамера;
- `memory_capacity` — обозначает емкость памяти фотокамеры для хранения
фотографий;
- `photos` — хранит фотографии, сделанные с помощью фотокамеры;
- `take_photo()` — имитирует съемку фотографии. Метод должен выводить
сообщение вида «Сделана фотография с разрешением [ширина]x[высота].»;
- `get_camera_info()` — возвращает строку с информацией о фотокамере в
формате «Марка: [марка], Модель: [модель], Разрешение:
[ширина]x[высота].»;
- `turn_on()` — включает фотокамеру. Метод должен установить значение
атрибута `is_on` в `True` и вывести сообщение «Фотокамера включена.»;
- `turn_off()` — выключает фотокамеру. Метод должен установить значение
атрибута `is_on` в `False` и вывести сообщение «Фотокамера выключена.»;
- `is_camera_on()` — возвращает логическое значение, указывающее,
включена ли фотокамера;
- `store_photo(photo)` — сохраняет фотографию `photo` в памяти
фотокамеры, если есть свободное место. Возвращает `True`, если фотография
успешно сохранена, и `False`, если память полна;
- `view_photos()` — выводит информацию о всех фотографиях, сохраненных
в памяти фотокамеры;
- `clear_memory()` — очищает память фотокамеры, удаляя все сохраненные
фотографии.
"""


class PhotoCamera:
    def __init__(self, brand, model, resolution, memory_capacity):
        self.brand = brand
        self.model = model
        self.resolution = resolution  # кортеж (width, height)
        self.is_on = False  # камера изначально выключена
        self.memory_capacity = memory_capacity
        self.photos = []  # изначально пустой список

    def take_photo(self):
        if self.is_on:
            print(f"Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]}.")
        else:
            print("Включите камеру!")

    def get_camera_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}."

    def turn_on(self):
        self.is_on = True
        print("Фотокамера включена.")

    def turn_off(self):
        self.is_on = False
        print("Фотокамера выключена.")

    def is_camera_on(self):
        return self.is_on

    def store_photo(self, photo):
        if len(self.photos) < self.memory_capacity:
            self.photos.append(photo)
            return True
        else:
            return False

    def view_photos(self):
        if self.photos:
            for photo in self.photos:
                print(photo)
        else:
            print("Нет сохраненных фотографий.")

    def clear_memory(self):
        self.photos = []


# Создание камеры
camera = PhotoCamera("Canon", "EOS R5", (8192, 5464), 3)

# Включение и съемка
camera.turn_on()
camera.take_photo()

# Информация о камере
print(camera.get_camera_info())

# Сохранение фотографий
print(camera.store_photo("photo1.jpg"))  # True
print(camera.store_photo("photo2.jpg"))  # True
print(camera.store_photo("photo3.jpg"))  # True
print(camera.store_photo("photo4.jpg"))  # False (память полна)

# Просмотр фотографий
camera.view_photos()

"""
## Задача 3
Напишите класс `Revolver` со следующей функциональностью:
- максимальная вместимость барабана — 6 элементов;
- метод `add_bullet(bullet)` добавляет патрон в ближайший свободный
слот барабана. Если добавление прошло успешно, возвращается `True`, иначе
`False`;
- метод `add_bullets_from_list(list)` добавляет патроны из списка в
барабан. Если в списке недостаточно патронов, барабан заполняется
настолько, насколько это возможно. При успешном добавлении любого
количества патронов метод возвращает `True`. В противном случае — если
список пустой, метод возвращает `False`;
- револьвер имеет указатель, который указывает на слот, из которого
револьвер готов произвести выстрел;
- метод `shoot()` удаляет патрон из слота, на который указывает
указатель, и передвигает указатель на следующий слот в барабане. Если
слот пустой, возвращается `None`;
- метод `unload(all_items=False)` извлекает все патроны из барабана или
только патрон, на который указывает указатель. Если `all_items=True`,
возвращается список всех патронов. Если `all_items=False`, возвращается
только патрон, на который указывает указатель. Если слот, на который
указывает указатель, пустой, метод возвращает `None`;
- метод `scroll()` перемещает указатель на случайный слот в барабане;
- метод `bullet_count()` возвращает количество патронов в барабане.
Проверьте результат: напишите код, который показывает, как работает класс
`Revolver`."""

import random


class Revolver:
    def __init__(self):
        self.cylinder = [None] * 6  # Барабан на 6 слотов
        self.pointer = 0  # Указатель на текущий слот

    def add_bullet(self, bullet):
        """Добавляет патрон в ближайший свободный слот"""
        for i in range(6):
            if self.cylinder[i] is None:
                self.cylinder[i] = bullet
                return True
        return False  # Барабан полон

    def add_bullets_from_list(self, bullet_list):
        """Добавляет патроны из списка в барабан"""
        if not bullet_list:  # Список пустой
            return False

        added_any = False
        for bullet in bullet_list:
            if self.add_bullet(bullet):
                added_any = True
            else:
                break  # Барабан полон

        return added_any

    def shoot(self):
        """Производит выстрел из текущего слота и перемещает указатель"""
        current_bullet = self.cylinder[self.pointer]
        if current_bullet is not None:
            self.cylinder[self.pointer] = None  # Удаляем патрон
            self.pointer = (self.pointer + 1) % 6  # Перемещаем указатель
            return current_bullet
        else:
            self.pointer = (self.pointer + 1) % 6  # Перемещаем указатель даже если слот пустой
            return None

    def unload(self, all_items=False):
        """Извлекает патроны из барабана"""
        if all_items:
            # Извлекаем все патроны
            bullets = [bullet for bullet in self.cylinder if bullet is not None]
            self.cylinder = [None] * 6
            return bullets
        else:
            # Извлекаем только патрон из текущего слота
            current_bullet = self.cylinder[self.pointer]
            if current_bullet is not None:
                self.cylinder[self.pointer] = None
                return current_bullet
            else:
                return None

    def scroll(self):
        """Перемещает указатель на случайный слот"""
        self.pointer = random.randint(0, 5)

    def bullet_count(self):
        """Возвращает количество патронов в барабане"""
        return sum(1 for bullet in self.cylinder if bullet is not None)

    def show_cylinder_state(self):
        """Вспомогательный метод для демонстрации состояния барабана"""
        state = []
        for i, bullet in enumerate(self.cylinder):
            if i == self.pointer:
                state.append(f"[{bullet if bullet else 'Empty'}]*")  # * указывает на текущий слот
            else:
                state.append(f"{bullet if bullet else 'Empty'}")
        return " | ".join(state)


# Демонстрация работы класса Revolver
print("=== Демонстрация класса Revolver ===\n")

# Создаем револьвер
revolver = Revolver()
print("1. Создан новый револьвер")
print(f"   Состояние барабана: {revolver.show_cylinder_state()}")
print(f"   Количество патронов: {revolver.bullet_count()}")

# Добавляем отдельные патроны
print("\n2. Добавляем патроны по одному:")
bullets = ["9mm", "45ACP", "357Mag"]
for bullet in bullets:
    result = revolver.add_bullet(bullet)
    print(f"   Добавляем {bullet}: {'Успешно' if result else 'Неудачно'}")
print(f"   Состояние барабана: {revolver.show_cylinder_state()}")
print(f"   Количество патронов: {revolver.bullet_count()}")

# Добавляем патроны из списка
print("\n3. Добавляем патроны из списка:")
more_bullets = ["38Special", "44Mag", "22LR", "50AE"]  # 4 патрона, но места только 3
result = revolver.add_bullets_from_list(more_bullets)
print(f"   Результат добавления: {'Успешно' if result else 'Неудачно'}")
print(f"   Состояние барабана: {revolver.show_cylinder_state()}")
print(f"   Количество патронов: {revolver.bullet_count()}")

# Пытаемся добавить еще один патрон (барабан полон)
print("\n4. Пытаемся добавить патрон в полный барабан:")
result = revolver.add_bullet("Extra")
print(f"   Результат: {'Успешно' if result else 'Барабан полон'}")

# Производим несколько выстрелов
print("\n5. Производим выстрелы:")
for i in range(3):
    shot = revolver.shoot()
    print(f"   Выстрел {i + 1}: {shot if shot else 'Холостой (пустой слот)'}")
    print(f"   Состояние после выстрела: {revolver.show_cylinder_state()}")

# Прокручиваем барабан
print("\n6. Прокручиваем барабан (scroll):")
print(f"   До прокрутки: {revolver.show_cylinder_state()}")
revolver.scroll()
print(f"   После прокрутки: {revolver.show_cylinder_state()}")

# Извлекаем один патрон
print("\n7. Извлекаем патрон из текущего слота:")
unloaded_bullet = revolver.unload()
print(f"   Извлеченный патрон: {unloaded_bullet if unloaded_bullet else 'Слот пустой'}")
print(f"   Состояние барабана: {revolver.show_cylinder_state()}")

# Извлекаем все патроны
print("\n8. Извлекаем все патроны:")
all_bullets = revolver.unload(all_items=True)
print(f"   Извлеченные патроны: {all_bullets}")
print(f"   Состояние барабана: {revolver.show_cylinder_state()}")
print(f"   Количество патронов: {revolver.bullet_count()}")

# Тестируем с пустым списком
print("\n9. Тестируем добавление из пустого списка:")
result = revolver.add_bullets_from_list([])
print(f"   Результат: {'Успешно' if result else 'Список пустой'}")

print("\n=== Конец демонстрации ===")