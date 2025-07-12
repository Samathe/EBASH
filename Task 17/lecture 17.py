def print_vars(x=None, y=None):
    print(f'{x=}')
    print(f'{y=}')


# *args

L1 = [235, 634, 73]
print(*L1)

L2 = [*L1, 213, 5, 435]
print(L2)


def visitors(teacher='AR', *students):
    print('The teacher is', teacher)
    print('The students are:')
    for student in students:
        print(student)


visitors('Hi', '32', '2325')


def visitors(teacher='AR', **students):
    print('The students and their tariffs are:')
    print(students)
    for st, tar in students.items():
        print(f'Student:{st} Tariff:{tar}')


visitors('Capybara', Petya = 'Base', Vanya = 'Standart', Andrey = 'Pro')
