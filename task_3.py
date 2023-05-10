"""
    Задача 3. 
    
    Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй.
    «one» «onetwonine» - o – 2, n – 3, e – 2
"""

def task_3():
    word = 'oneo'
    phrase = 'onetwonine'
    used = []
    for el in word:
        count = 0
        if not el in used:
            for letter in phrase: 
                if letter == el:
                    count += 1
                used.append(el)
            print(f'{el} - {count}')
        else:
            print(f'{el} - уже втречался')
task_3()

