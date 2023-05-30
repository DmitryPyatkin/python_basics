"""
    Задача 1. Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.
"""
import numpy as np

array_of_elements = [1,2,2,1,3,4,5,5,5]
print(array_of_elements)
unique, counts = np.unique(array_of_elements, return_counts=True)
for i, j in zip(unique, counts):
    print(f'Элемент {i} встречается в массиве {j} раз')