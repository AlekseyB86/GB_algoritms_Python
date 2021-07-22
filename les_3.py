def task_1() -> None:
    """1. В диапазоне натуральных чисел от 2 до 99 определить,
     сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

    for num in range(2, 10):
        print(f'{num}: {len([el for el in range(2, 100) if el % num == 0])}')


def task_2() -> None:
    """2. Во втором массиве сохранить индексы четных элементов первого массива.
    Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
    надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается
    с нуля), т.к. именно в этих позициях первого массива стоят четные числа."""

    fist_array = [8, 3, 15, 6, 4, 2]
    print(*fist_array)
    second_array = [idx + 1 for idx in range(len(fist_array)) if fist_array[idx] % 2 == 0]
    print(*second_array)


def task_3() -> None:
    """3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

    nums = [8, 3, 15, 6, 4, 2]
    # nums = [1, 1, 1, 1]
    print(*nums)

    # 1 variant
    idx_mx = nums.index(max(nums))
    idx_mn = nums.index(min(nums))
    if idx_mx == idx_mn:
        print('There is no maximum or minimum element in the array')
    else:
        nums[idx_mn], nums[idx_mx] = max(nums), min(nums)
        print(*nums)

    # # 2 variant
    # mx = mn = nums[0]
    # idx_mx = idx_mn = None
    # for idx, num in enumerate(nums):
    #     if mx < num:
    #         mx, idx_mx = num, idx
    #     if mn > num:
    #         mn, idx_mn = num, idx
    # if idx_mx == idx_mn:
    #     print('There is no maximum or minimum element in the array')
    # else:
    #     nums[idx_mx], nums[idx_mn] = mn, mx
    #     print(nums)


def task_4() -> None:
    """4. Определить, какое число в массиве встречается чаще всего."""

    nums = [3, 12, 34, 658, 3, 94, 456, 45, 8, 9, 12, 3, 76, 987]
    print(*nums)
    cnt = 0
    num = None
    for el in nums:
        if nums.count(el) > cnt:
            cnt = nums.count(el)
            num = el
    print(f'Number {num} occurs most often: {cnt} times')


def task_5() -> None:
    """5. В массиве найти максимальный отрицательный элемент.
    Вывести на экран его значение и позицию в массиве."""

    nums = [-12, 0, -999, 34, 4, -5]
    print(*nums)
    mx_el = min(nums)
    print(mx_el)
    pos_el = None
    for el in range(len(nums)):
        if 0 > nums[el] > mx_el:
            mx_el = nums[el]
            pos_el = el + 1
    if not pos_el:
        print('There are no negative elements in the array!')
    else:
        print(f'Max negative element: {mx_el} pos {pos_el}')


def task_6() -> None:
    """6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать."""

    nums = [12, 0, -9, 34, 4, -5]
    print(*nums)
    # # 1 variant
    # print('Sum of elements between max and min: ', sum(nums) - min(nums) - max(nums))

    # 2 variant
    nums.sort()
    print('Sum of elements between max and min: ', sum(nums[1:-1]))


def task_7() -> None:
    """7. В одномерном массиве целых чисел определить два наименьших элемента.
    Они могут быть как равны между собой (оба являться минимальными), так и различаться."""

    nums = [-9, 0, -9, 34, 4, -5]
    nums.sort()
    print('The two smallest elements:', *nums[:2])


def task_8() -> None:
    """8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
    Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
    в последнюю ячейку строки. В конце следует вывести полученную матрицу."""


def task_9() -> None:
    """9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    task_7()
    # task_8()
    # task_9()
