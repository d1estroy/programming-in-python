# Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.

a = int(input()) 
s = 0              
while a != 0:    
    s += a      
    a = int(input())     
print(s)

