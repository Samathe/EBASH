def devision(text):
    a, b = map(int, text.split('/'))

    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return 'ERROR'


print(devision("555 / 0"))


def check_password(*passwords):
    result = []

    for password in passwords:
        try:
            int(password, 16)
            result.append(password)
        except ValueError:
            pass
    return result


print(check_password("password", "123456", "abcdef", "bcdefg"))

olympiad1 = {"name": "Пробная вышка",
             "winners": {
                 "Олеся Олимпиадникова": 594,
                 "Олег Олимпиадников": 587,
                 "Онисим Олимпиадников": 581,
             }}
olympiad2 = {"name": "Горные воробьи",
                          "winners": {
                              "Ольга Олимпиадникова": (20, 20, 19, 20),
                              "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
                              "Офелия Олимпиадникова": (20, 20, 20, 20, 13)
                          }}


def checkOlympiads(name):
    try:
        points1 = olympiad1["winners"][name]
        print(f'[{olympiad1["name"]}] победитель {points1}')
    except KeyError:
        print(f'[{olympiad1["name"]}] призёр')
    finally:
        print("-" * 20)

    try:
        points2 = olympiad2["winners"][name][4]
        print(f'[{olympiad2["name"]}] победитель {points2}')
    except IndexError:
        print(f'[{olympiad2["name"]}] победитель')
    except KeyError:
        print(f'[{olympiad2["name"]}] призёр')
    finally:
        print("-" * 20)
checkOlympiads("Ольга Олимпиадникова")
checkOlympiads("Олеся Олимпиадникова")

"""[Пробная вышка] призёр
--------------------
[Горные воробьи] победитель
--------------------
[Пробная вышка] победитель 594
--------------------
[Горные воробьи] победитель 17
--------------------"""

def terribly_impolite_program():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Ты не пройдёшь!")
        terribly_impolite_program()
terribly_impolite_program()


class LizardInCup(Exception):
    pass

class BarBurntDown(Exception):
    pass

def orderBeer():
    try:
        mugs = input("\nВы заходите в бар. "
                     "Сколько кружек лимонада заказываете?\n").lower()

        if mugs == "ящерица в стакане":
            raise LizardInCup

        if mugs == "где туалет?":
            raise BarBurntDown

        mugs = int(mugs)
        assert mugs < 2, "Кризис. Не больше одной кружки в одни руки."

        if mugs <= 0 or mugs >= 100:
            raise ValueError

    except AssertionError:
        print("Кризис. Не больше одной кружки в одни руки.")

    except ValueError:
        print("Вы не можете заказать такое число кружек, держите одну кружку.")

    except LizardInCup:
        print("У нас закончились ящерицы. Приходите завтра!")

    except BarBurntDown:
        print("Поздравляем! Бар сгорел. Вы вышли из симуляции.")
        return

    else:
        print("Приходите ещё!")

orderBeer()
orderBeer()
