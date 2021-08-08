# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def get_count_unique_substrings(strings: str) -> int:
    """
    Определяет количество различных подстрок с использованием хеш-функции.
    В сумму не включается пустуя строка и строка целиком.
    :param strings: строка в которой происходит поиск подстрок
    :return : кол-во уникальных подстрок
    """
    unique_substrings = set()
    for j in range(1, len(strings)):
        for i in range(len(strings)):
            substrings = strings[i:i + j]
            if substrings not in ['', strings]:
                unique_substrings.add(hashlib.sha1(substrings.encode('utf-8')).hexdigest())
    return len(unique_substrings)


my_strings = input('Enter string: ')
print(f'Number of unique substrings: {get_count_unique_substrings(my_strings)}')
