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


def save():
    with open('Многочлен.txt', "w") as data:
        data.write(list_1)
        print("Успешное сохранение в Многочлен.txt")
        data.close()


try:
    print('Для создания многочлена введите степень')
    k = int(input('Задайте натуральную степень: '))
    if k <= 0:
        print('Введите целое число больше 0')
    else:    
        list_k = create_ratio_list(k)
        result_polynomial = create_polynomial(list_k, k)
        list_1 = ''.join(map(str, result_polynomial))
        print(list_1)
        save()    
except:
    print('Введите целое число больше 0')


