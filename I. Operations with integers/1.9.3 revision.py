"""
Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
"""

# Считывание входных данных
first_num = float(input())
second_num = float(input())
operation = input()

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "/":
    if second_num == 0:
        print("Деление на 0!")
    else:
        print(first_num / second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "mod":
    if second_num == 0:
        print("Деление на 0!")
    else:
        print(first_num % second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "div":
    if second_num == 0:
        print("Деление на 0!")
    else: 
        print(first_num // second_num)
