"""
    Задача 1. 
    
    Дано натуральное число N. Найдите значение выражения: N + NN + NNN
    N может быть любой длины.
    N = 132:132 + 132132 + 132132132 = 132264396
"""

n = 132
result = n + n * 2 + n * 3 
print(result) # -> 738

n = '132'
result = n + n * 2 + n * 3 
print(result) # -> 123 123123 123123123

n = '132'
result = int(n) + int(n * 2) + int(n * 3) 
print(result) # -> 132264396

def task_1():
    n = input('Введите число: ')
    m = int(input('Введите количество преобразований числа: '))
    sum = 0
    for i in range(1, m + 1):
        num = n * i
        print(num)
        sum = (sum + int(num))
        print(sum)
task_1()