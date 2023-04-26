"""
    Задача 2. 
    
    Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
    [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
    [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
"""
import random
def task_2():
    massiv = [random.randint(0, 9) for _ in range(15)]
    print(massiv)
    number = input('Введите число: ')

    res = []
    for el in number:
        res.append(int(el))
    
    result = False
    for i in range(len(massiv) - len(res)):
        if res == massiv[i:len(res) + i]:
            result = True
    
    if result == True:
        print(f'{massiv} - {res} -> да')
    else:
        print(f'{massiv} - {res} -> нет')
        
task_2()