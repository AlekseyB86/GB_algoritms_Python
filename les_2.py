from random import randint


def task_1() -> None:
    """1. Написать программу, которая будет складывать, вычитать,
    умножать или делить два числа. Числа и знак операции вводятся пользователем.
    После выполнения вычисления программа не должна завершаться, а должна
    запрашивать новые данные для вычислений. Завершение программы должно
    выполняться при вводе символа '0' в качестве знака операции.
    Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
    то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
    Также сообщать пользователю о невозможности деления на ноль,
    если он ввел 0 в качестве делителя."""

    while True:
        operator = input('Enter the operation sign (0 - quit): ').strip()
        if operator == '0':
            break
        elif len(operator) != 1 or operator not in ['/', '*', '+', '-']:
            print('Invalid operation sign entered! (/, *, +, -)')
            continue
        else:
            num_1, num_2 = map(float, input('Enter numbers by a space: ').split())
        if operator == '/':
            if num_2 == 0:
                print('Cannot divide by zero')
                continue
            result = num_1 / num_2
        elif operator == '*':
            result = num_1 * num_2
        elif operator == '+':
            result = num_1 + num_2
        else:
            result = num_1 - num_2
        print(f'Result: {num_1} {operator} {num_2} = {result:.2f}')
    print('END.')


def task_2() -> None:
    """2. Посчитать четные и нечетные цифры введенного натурального числа.
    Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""
    # 1 variant
    # nums = input('Enter a natural number: ')
    # nums_lst = list(map(int, nums))
    # even_nums = []
    # odd_nums = []
    # while nums_lst:
    #     num = nums_lst.pop()
    #     even_nums.append(num) if num % 2 == 0 else odd_nums.append(num)

    # 2 variant
    nums_lst = list(map(int, input('Enter a natural number: ')))
    even_nums = [num for num in nums_lst if num % 2 == 0]
    odd_nums = [num for num in nums_lst if num % 2 != 0]
    print(f'Count even numbers: {len(even_nums)} {even_nums}')
    print(f'Count odd numbers: {len(odd_nums)} {odd_nums}')


def task_3() -> None:
    """3. Сформировать из введенного числа обратное по порядку входящих в него цифр
    и вывести на экран. Например, если введено число 3486, то надо вывести число 6843."""

    # 1 variant
    num = list(map(str, input('Enter a natural number: ')))
    new_num = []
    while num:
        new_num.append(num.pop())
    new_num = int("".join(new_num))
    print(new_num)

    # 2 variant
    # print(int(input('Enter a natural number: ')[::-1]))

    # 3 variant
    # print(int("".join(reversed(input('Enter a natural number: ')))))


def task_4() -> None:
    """4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
    Количество элементов (n) вводится с клавиатуры."""

    # # 1 variant
    # n = int(input('Enter number n:'))
    # num = -2
    # nums = []
    # for _ in range(n):
    #     num /= -2
    #     nums.append(num)
    # print(f'Сумма элементов ряда чисел: {" ".join(map(str, nums))} = {sum(nums)}')

    # 2 variant
    n = int(input('Enter number n:'))
    m = -2

    def recursion(x, y):
        y /= -2
        if x == 1:
            return y
        return y + recursion(x - 1, y)

    print(f'Сумма элементов ряда чисел: {recursion(n, m)}')


def task_5() -> None:
    """5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
    и заканчивая 127-м включительно. Вывод выполнить в табличной форме:
    по десять пар "код-символ" в каждой строке."""

    pair = 10
    start = 32
    end = 127
    chars = []
    for el in range(end - start + 1):
        chars.append(f'{start}-{chr(start)}')
        start += 1
        pair -= 1
        if start == end + 1 or pair == 0:
            print('  '.join(chars) + '\n')
            pair = 10
            chars = []


def task_6() -> None:
    """6. В программе генерируется случайное целое число от 0 до 100.
    Пользователь должен его отгадать не более чем за 10 попыток.
    После каждой неудачной попытки должно сообщаться больше или меньше
    введенное пользователем число, чем то, что загадано.
    Если за 10 попыток число не отгадано, то вывести загаданное число."""

    num = randint(0, 100)
    # print(num)
    cnt_try = 10
    while cnt_try > 0:
        num_user = int(input(f'Try №{cnt_try}. Enter the hidden number: '))
        if num_user == num:
            print(f'Congratulations! You guessed the number "{num}" on the {cnt_try}th try!')
            break
        elif num_user > num:
            print('The entered number is greater')
        else:
            print('The entered number is less')
        cnt_try -= 1
        if cnt_try == 0:
            print(f'You lose! The hidden number: "{num}"')
            break
    print('END.')


def task_7() -> None:
    """7. Напишите программу, доказывающую или проверяющую, что для множества
    натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
    где n - любое натуральное число."""


def task_8() -> None:
    """8. Посчитать, сколько раз встречается определенная цифра в введенной
    последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
    посчитать, задаются вводом с клавиатуры."""


def task_9() -> None:
    """9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
    Вывести на экран это число и сумму его цифр."""


if __name__ == "__main__":
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    task_7()
    # task_8()
    # task_9()
