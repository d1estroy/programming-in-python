"""
Напишите программу, которая считывает с клавиатуры два числа 
a и b, считает и выводит на консоль среднее арифметическое всех чисел из отрезка 
[a;b], которые кратны числу 3.

В приведенном ниже примере среднее арифметическое считается для чисел на отрезке 
[−5;12]. Всего чисел, делящихся на 3, на этом отрезке 6: −3,0,3,6,9,12. Их среднее арифметическое равно 4.5

На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3.
"""

a = int(input()) # Ввод первого числа (a)
b = int(input()) # Ввод второго числа (b)

sum = 0 # Инициализация переменной для суммы чисел, кратных 3
count = 0 # Инициализация переменной для количества чисел, кратных 3

# Цикл по всем числам в диапазоне от a до b
for i in range(a, b + 1):
    if i % 3 == 0: # Проверка, делится ли число i на 3 без остатка
        sum += i # Если делится, то добавляем его к сумме
        count += 1 # Увеличиваем счетчик

# Вычисление среднего арифметического
average = sum / count

# Вывод результата
print(average)
