"""
    Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.
"""

def repeat_func(times):
    def procedure(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return procedure

@repeat_func(times=6)
def func():
    print("Hello")

func()
