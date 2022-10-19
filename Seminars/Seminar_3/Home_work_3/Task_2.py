# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def create_list(size):
    list = [0] * size
    for i in range(size):
        try:
            list[i] = int(input(f'Введите значение {i + 1}: '))
        except:
            print('Введите число')
    return list


def multipli_elements(array):
    length = len(array)
    if length % 2 == 0:
        half_len = int(length/2)
        res_list = [0] * half_len
        for i in range(half_len):
            res_list[i] = array[i] * array[(i + 1) * (-1)]
        return res_list
    else:
        half_len = int(length/2)
        res_list = [0] * (half_len + 1)
        for i in range(half_len):
            res_list[i] = array[i] * array[(i + 1) * (-1)]
        res_list[-1] = array[half_len] ** 2
        return res_list


try:
    size = int(input('Введите размер списка: '))
    list_1 = create_list(size)
    print(f'Исходный список: {list_1}')
    result = multipli_elements(list_1)
    print(f'Произведение пар чисел списка: {result}')
except:
    print('Введите число!')
