"""
    Задача 3. 
    
    Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй.
    «one» «onetwonine» - o – 2, n – 3, e – 2
"""

def task_3():
    word = 'one'
    phrase = 'onetwonine'

    for el in word:
        count = 0
        for letter in phrase: 
            if letter == el:
                count += 1
        print(f'{el} - {count}')
task_3()

