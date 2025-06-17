#1 True
#2
"""
password1 = input()
password2 = input()

if password1 == password2:
    print(True)
else:
    print(False)
Answer: False
"""
#3
"""a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a >= b) and (a >= c) and (a >= d):
    print(a)
else:
    if (b >= c) and (b >= d):
        print(b)
    else:
        if (c >= d):
            print(c)
        else:
            print(d)
#Answer: 12 
"""
#5
"""a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print(True)
else:
    print(False)"""
# Answer : True
#6
"""a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    if (a != b != c):
        print("Разностороний")
    if (a == b == c):
        print("Равностороний")
else:
    print("Вырожденный")"""
#Answer : Вырожденный
# 7

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b < c or d < a :
    print(0)
elif (c >= a and d <= b ):
    print(d - c + 1)
elif (a >= c and b <= d ):
    print(b - a + 1)
elif (b >= c and b <= d and a <= c):
    print(b - c + 1)
elif (d >= a and d <= b and c <= a):
    print(d - a + 1)
