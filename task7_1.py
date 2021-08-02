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
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def sort_p_mod(a: list) -> list:  # Пузырьковая сортировка улучшеная версия
    """Модификация пузырьковой сортировки - уменьшено количество проходов"""
    rev = 1
    start = 0
    tmp = None
    end = len(a) - 1
    for _ in range(end + 1):
        if rev > 0:
            for i in range(start, end):
                tmp = a[i]
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
            end -= 2 if tmp == a[end - 1] else 1
        else:
            for i in range(end - start):
                tmp = a[end - i]
                if a[end - i] < a[end - i - 1]:
                    a[end - i], a[end - i - 1] = a[end - i - 1], a[end - i]
            start += 2 if tmp == a[end - i] else 1
        rev *= -1
        if end == 1:
            break
    return a


nums = [randint(-100, 100) for _ in range(1000)]
# nums = [65, 96, 84, 49, 93, -63, -58, -33, -5, 25]
print(nums)
nums_cp = nums.copy()

cProfile.run('sort_p(nums)')
print(sort_p(nums))
cProfile.run('sort_p_mod(nums_cp)')
print(sort_p_mod(nums_cp))
