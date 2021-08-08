# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def quick_select_median(lst: list, pivot_fn=random.choice) -> float:
    if len(lst) % 2 == 1:
        return quick_select(lst, len(lst) // 2, pivot_fn)
    else:
        return 0.5 * (quick_select(lst, len(lst) // 2 - 1, pivot_fn) +
                      quick_select(lst, len(lst) // 2, pivot_fn))


def quick_select(lst: list, k: int, pivot_fn) -> int:
    """
    Выбираем k-тый элемент в списке lst (с нулевой базой)
    :param lst: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент lst
    """
    if len(lst) == 1:
        assert k == 0
        return lst[0]

    pivot = pivot_fn(lst)

    lows = [el for el in lst if el < pivot]
    highs = [el for el in lst if el > pivot]
    pivots = [el for el in lst if el == pivot]

    if k < len(lows):
        return quick_select(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quick_select(highs, k - len(lows) - len(pivots), pivot_fn)


m = 5
arr = [int(random.uniform(-50, 50)) for _ in range(2 * m + 1)]
print(arr)
print(f'Медиана массива: {quick_select_median(arr)}')
