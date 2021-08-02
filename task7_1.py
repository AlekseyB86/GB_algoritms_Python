"""Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""

from random import randint
import cProfile


def sort_p(lst: list) -> list:  # Пузырьковая сортировка из урока
    length = len(lst)
    for k in range(1, length):
        for i in range(length - k):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def sort_p_mod(a: list, direction=True) -> list:  # Пузырьковая сортировка улучшеная версия
    """Модификация пузырьковой сортировки - уменьшено количество проходов"""
    k = 1
    rev = 1
    for n in range(len(a) // 2):
        if rev > 0:
            for i in range(len(a) - k):
                if a[i] > a[i+1] and direction:
                    a[i], a[i+1] = a[i+1], a[i]
                else:

        else:
            for i in range(k, len(a) - k, -1):
                if a[i] > a[i-1]:
                    a[i], a[i - 1] = a[i - 1], a[i]
        rev *= -1
    return a


nums = [randint(-100, 99) for _ in range(10)]
print(nums)
nums_cp = nums.copy()

# cProfile.run('sort_p(nums)')
print(sort_p(nums))
# cProfile.run('sort_p_mod(nums_cp)')
print(sort_p_mod(nums_cp))
