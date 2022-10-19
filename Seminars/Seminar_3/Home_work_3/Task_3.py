# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from fractions import Fraction

def create_list(size):
    list = [0] * size
    for i in range(size):
        try:
            list[i] = float(input(f'Введите вещественное число {i + 1}: '))
        except:
            print('Введите число, используя "." !')
    return list

def diff_max_min_fract(list):
    for i in range(len(list)):
        list[i] = list[i] - int(list[i])        # Отделяем дробную часть от числа 
        list[i] = Fraction.from_float(list[i])
    min = list[0]
    max = list[0]
    for i in range(len(list)-1):
        if min > list[i + 1]:
            min = list[i + 1]
        else:
            max = list[i + 1]
    fract = max - min
    result = fract.numerator / fract.denominator # Получаем вещественное число
    return result

try:
    size = int(input('Введите размер списка: '))
    list_1 = create_list(size)
    print(f'Исходный список: {list_1}')
    res = diff_max_min_fract(list_1)
    print(f'Разница между максимальным и минимальным \
значением дробной части элементов: {round(res, 3)}')

except:
    print('Введите вещественное число используя "." или целое число!')