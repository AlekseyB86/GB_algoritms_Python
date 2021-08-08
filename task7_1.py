"""Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее)."""

from random import randint


def sort_p(lst: list) -> list:  # Пузырьковая сортировка из урока
    length = len(lst)
    for k in range(1, length):
        for i in range(length - k):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def sort_p_mod(lst: list, direction=True) -> list:    # Пузырьковая сортировка улучшеная версия
    """
    Пузырьковая сортировка модифицированная - добавлен реверс:
     добавлен ранний выход из функции, если значения не менялись местами в одной итерации,
     что сокращает время работы функции при большем кол-ве данных
    :param lst: массив чисел
    :param direction: по умолчанию True - на увеличение, False - на убывание
    :return list: отсортированный массив чисел
    """

    length = len(lst)
    for j in range(1, length):
        need_sort = False  # триггер на сортировку
        for i in range(length - j):
            if direction and lst[i] > lst[i + 1]:  # сортироуем на убывание или на возрастание
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                need_sort = True
            elif lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                need_sort = True
        if not need_sort:  # сортируем?
            break
    return lst


nums = [randint(-100, 99) for _ in range(10)]
print(nums)
nums_cp = nums.copy()
print(sort_p(nums))
print(sort_p_mod(nums_cp, False))
