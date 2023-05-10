"""
    Задача 2. 
    
    Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
"""
def task_2():
    print('¬(X ∧ Y) ∨ Z')
    for x in range (0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} | {int(not (x or y) and z)}')
task_2()