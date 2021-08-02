"""Подсчитать, сколько в программе было выделено памяти под переменные.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Результаты анализа вставьте в виде комментариев к коду.
Напишите в комментариях версию Python и разрядность ОС."""

import random
import sys


def get_total_size(lst):
    total_size = 0
    for itm in lst:
        print(f'type = {type(itm)}, size = {sys.getsizeof(itm)}, object = {itm}')
        total_size += sys.getsizeof(itm)
    print(f'\nПамяти под переменные:\n{total_size} байт\n')


# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

nums = [random.randint(0, 100) for _ in range(10)]
print(nums)

print('\nВариант 1')
min_num = max_num = nums[0]
min_idx = max_idx = 0

for i in range(len(nums)):
    if nums[i] < min_num:
        min_num = nums[i]
        min_idx = i
    if nums[i] > max_num:
        max_num = nums[i]
        max_idx = i
tmp = nums[min_idx]
nums[min_idx] = nums[max_idx]
nums[max_idx] = tmp

print(f'{nums} - перестановка')

# Подсчет использования памяти
var_list = [nums, min_num, min_idx, max_num, max_idx, tmp, i]
get_total_size(var_list)

# Вариант 2
print('Вариант 2')
nums[nums.index(max(nums))], nums[nums.index(min(nums))] = nums[nums.index(min(nums))], nums[nums.index(max(nums))]
print(f'{nums} - перестановка')

# Подсчет использования памяти
var_list = [nums, max(nums), min(nums)]
get_total_size(var_list)


print(f'Версия Python и разрядность OS\n{sys.version}')

# Выводы:
# За счет меньшего числа промежуточных переменных, второй вариант решения задачи менее затратен по памяти:
# 240 против 352 байт
