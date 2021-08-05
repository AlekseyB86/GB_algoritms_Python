# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

from random import shuffle, random
import operator


def merge_sort(arr: list, compare=True) -> list:
    """Сортировка методом слияния, по умолчанию True- сортировка на возрастание, False- на убывание """
    if len(arr) < 2:
        return arr[:]

    middle = len(arr) // 2  # разделение массива на две части
    left = merge_sort(arr[:middle], compare)
    right = merge_sort(arr[middle:], compare)

    return merge(left, right, compare)


def merge(left, right, compare) -> list:
    # сравнивает числа левого и правого и возвращает масив отсортированх чисел
    result = []
    i, j = 0, 0
    compare = operator.lt if compare else operator.gt
    # сравнение чисел из левого и парвого и добавление их в новый массив
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # добавление в конец массива остальных чисел из левого либо правого, которые остались после сравнения
    result.extend(left[i:]) if j > i else result.extend(right[j:])

    return result


if __name__ == '__main__':
    nums = [round(50 * (1 - random()), 2) for _ in range(10)]
    print(f'исходный массив:\n{nums}')
    print(f'Масиив псле сортировки:\n{merge_sort(nums, False)}')
