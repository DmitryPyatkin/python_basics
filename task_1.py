"""
    Задача 1. 
    
    Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
    2, 3, 4, 6, 7, 8 -> 6, 7, 8
"""
import random
def task_1():

    length = int(input('Введите число: '))
    numbers = [random.randint(1, 11) for _ in range(length)]
    x = filter(lambda x: x > 5, numbers)
    x = list(x)
    print(length,'->', *x, end='')

task_1()
    
