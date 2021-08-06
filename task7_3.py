# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

from random import random


def get_median(lst: list) -> int:
    """
    Функция нахождения индекса медианы в массиве
    :param lst:
    :return: index median
    """
    median = lst[len(lst) // 2]
    less = [el for el in lst if el < median]
    greater = [el for el in lst if el > median]
    delta = len(less) - len(greater)
    while delta:
        if delta > 0:
            greater.append(median)
            median = max(less)
            less.remove(max(less))
        else:
            less.append(median)
            median = min(greater)
            greater.remove(min(greater))
        delta = len(less) - len(greater)

    return median


m = 10
arr = [int(100 * random()) for _ in range(2 * m + 1)]
print(arr)
print(f'Медиана массива: {get_median(arr)}')
