"""
    Задача 3. Создайте двумерный массив случайного размера. Найдите индексы максимального и минимального элементов в нём.
    Выведите элементы главной диагонали матрицы в виде одномерного массива.
"""
import numpy as np

x = np.random.randint(1, 10)
y = np.random.randint(1, 10)
array = np.random.randint(10, size=(x, y))

print(array)
print(f'Максимальный элемент массива имеет индекс: [{np.argmax(array, axis=0)[0]}, {np.argmax(array, axis=1)[0]}]')
print(f'Минимальный элемент массива имеет индекс: [{np.argmin(array, axis=0)[0]}, {np.argmin(array, axis=1)[0]}]')
print(f'Элементы главной диагонали массива: {array.diagonal()}')