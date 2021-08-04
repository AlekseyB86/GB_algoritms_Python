# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import random


def get_numb() -> float:
    number = 50*(1 - random())
    return round(number, 2)


nums = [get_numb() for _ in range(10)]
print(nums)
