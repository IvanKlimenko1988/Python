# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint, random


def create_ratio_list(num):
    ratio = []
    while num > 0:
        ratio.append(randint(0, 100))
        num -= 1
    return ratio


def create_polynomial(ratio_list, k):
    polynomial = []

    for i in range(len(ratio_list)):
        if ratio_list[i] == 0:
            continue
        elif ratio_list[i] == 1:
            polynomial.append('x')
            if k == 1:
                polynomial.append(' + ')
            else:
                polynomial.append('^')
                polynomial.append(k)
                polynomial.append(' + ')
                k -= 1
        else:
            polynomial.append(ratio_list[i])
            polynomial.append('x')
            if k != 1:
                polynomial.append('^')
                polynomial.append(k)
                polynomial.append(' + ')
                k -= 1
            else:
                polynomial.append(' + ')

    polynomial.append(randint(0, 100))

    if polynomial[-1] == 0:
        polynomial.remove(0)
        polynomial.remove(' + ')
    polynomial.append(' = 0')
    return polynomial


try:
    print("Cоздание случайного многочлена")
    k = int(input("Задайте натуральную степень 'k': "))
    if k > 0:
        ratio_array = create_ratio_list(k)
        result_polymomial = create_polynomial(ratio_array, k)
        print(''.join(map(str, result_polymomial)))
    else:
        exit()
except:
    print("Введите целое число 'k' > 0")
