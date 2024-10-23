"""
Сколько всего знаков * будет выведено после исполнения фрагмента программы:

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1
"""

i = 0
count =''
while i < 5:
    count +='*'
    if i % 2 == 0:
        count +='**'
    if i > 2:
        count +='***'
    i = i + 1

print(len(count)) # => 17