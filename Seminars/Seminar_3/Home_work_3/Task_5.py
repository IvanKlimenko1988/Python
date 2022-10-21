# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) ,
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей.
#
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился
# на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре,
# то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

from itertools import count
from random import Random, randint
import random

def create_2d_list(m, n):
    list_2d = []
    for i in range(m):
        list = []
        for j in range(n):
            # Заполним список случайными целыми числами [10, 99]
            list.append(randint(10, 99))
        list_2d.append(list)             # Добавим список в спикок
    return list_2d


def print_2d_list(array):
    for i in range(len(array)):
        print(' '.join(map(str, array[i])))


def mix_2d_list(list):
    list_1 = []
    for i in range(len(list)):
        for j in range(len(list[i])):
            list_1.append(list[i][j])
    chet = 0
    for i in range(int(len(list_1)/2)):
        rand_index = randint(0, len(list_1) - 1)
        temp = list_1[i]
        list_1[i] = list_1[rand_index]
        list_1[rand_index] = temp
        chet +=1
    print(f'Количество итераций = {chet}')
    k = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] = list_1[k]
            k += 1
    return list

try:
    print("Создание массива с чётным количеством элементов")
    rows = int(input('Введите колличество строк: '))
    columns = int(input('Введите колличество столбцов: '))
    if (rows * columns) % 2 == 0:
        start_array = create_2d_list(rows, columns)
        print('Исходный массив:')
        print_2d_list(start_array)
        res_array = mix_2d_list(start_array)
        print('Перемешенный исходный массив:')
        print()
        print_2d_list(res_array)

    else:
        print('Количество элементвов в массиве нечётное!')
        print('Завершение программы')
        exit()
except ValueError:
    print('Введите целое число')
print('Завершение программы')
