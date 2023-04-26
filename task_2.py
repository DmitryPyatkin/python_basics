"""
    Задача 2. 
    
    Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
    [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.
"""

import random


def task_2():
    n = random.randint(3, 10)
    numbers = [random.randint(1, 10) for _ in range(n)]
    print(numbers)
    length = len(numbers)
    j = 0
    while j < length:
        result = []
        min = numbers[j]
        result.append(min)
        i = j + 1
        flag1 = True
        while flag1:
            if result[len(result) - 1] < min:
                result.append(min)
            if i == length:
                flag1 = False
                continue
            flag = True
            while flag:
                if min < numbers[i]:
                    min = numbers[i]
                    i += 1
                    flag = False
                else:
                    i += 1
                    flag = False
        if len(result) > 1:
            print(result)
        j += 1
task_2()
