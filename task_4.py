"""
    Задача 4. 
    
    Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
    3 -> [2, 3, -3, -2, -1, 0, 1]
"""

def task_4():
    length = int(input('Введите число: '))
    length = abs(length)
    # Функция abs в Python возвращает абсолютное значение числа. Таким образом результат всегда положительный.
    numbers = []
    for num in range(-length, length + 1):
        numbers.append(num)
    print(numbers)

    step = int(input('Введите сдвиг: '))
 
    res = numbers[-step:] + numbers[: -step]
    print(res)

task_4()