""" 
    Задача 3. 
    Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
    [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. 
    Список уникальных элементов [1, 4, 2, 3, 6, 7]                                                                       
"""

import random

def task_3():
    nums = [random.randint(0, 10) for _ in range(10)]
    print(nums)
    unique = list(set(nums))
    repeat_sum = 0
    len_unique = len(unique)
    for i in range(len_unique):
        repeat = 0
        repeat = nums.count(unique[i])
        if repeat > 1:
            repeat_sum += repeat
            print(f'{unique[i]} - {repeat}')
    print(f'{repeat_sum} элемента совпадают')
    print(f'Список уникальных элементов: ', unique)
task_3()   