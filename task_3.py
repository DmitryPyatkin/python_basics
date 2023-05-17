"""
    Задача 3. 
    
    Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
"""

# def prostoe(n: int):
#     prostie_chisla = [2]
#     for i in range(3, n + 1, 2):
#         simple_number = True
#         q = int(n**0.5) + 2
#         for j in prostie_chisla:
#             if j > q:
#                 break
#             if i % j == 0:
#                 simple_number = False
#                 break
#         if simple_number == True:
#             prostie_chisla.append(i)
#         return prostie_chisla

# def drobi():
#     k = int(input('Минимальные знаменатель: '))
#     simple = prostoe(k)
#     n = 1
#     while n < k:
#         m = 2
#         while m <= k:
#             if m / n > 1:
#                 if n == 1:
#                     print(f'{n} / {m}')
#                 for i in simple:
#                     if n % i == 0 and m % i == 0:
#                         m+= 1
#                     continue
#                 if m % n != 0:
#                     print(f'{n} / {m}')
#             m += 1
#         n += 1
# drobi()

def check(x, y):
    for div in range(2, x + 1):
        if x % div == 0 and y % div == 0:
            return False
    return True

for y in range(2, 12):
    for x in range(1, y):
        if check(x, y):
            print(f'{x}/{y}', end=' ')
        print()
