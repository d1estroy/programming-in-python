"""
Жители страны Малевии часто экспериментируют с планировкой комнат. Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь, требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры, которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

Формат ввода, который используют Малевийцы:

треугольник
где a, b и c — длины сторон треугольника

прямоугольник
где a и b — длины сторон прямоугольника

круг
где r — радиус окружности.
"""

x = str(input())
if x == ('треугольник'):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) * 0.5
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5) 
elif x == ("прямоугольник"):
    a = int(input())
    b = int(input())
    print(a * b)
elif x == ("круг"):
    r = int(input())
    print(3.14 * r ** 2) 
