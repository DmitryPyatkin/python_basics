"""
    Задача 1. 
    
    Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
    6 –> 1 1 2 3 5 8
"""
import random
def task_1():
    
    fib1 = fib2 = 1
    
    length = int(input('Введите число: '))
    numbers = [random.randint(0, 25) for el in range(length)]
    print(length,'->',fib1, fib2, end=' ')
    
    for i in range(2, len(numbers)):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')

task_1()
    
