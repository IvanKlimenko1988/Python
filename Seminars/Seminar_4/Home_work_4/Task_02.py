# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def create_list(size):
    new_list = [0]*size
    for i in range(len(new_list)):
        new_list[i] = int(input("Введите число: "))
    return new_list


def show_uniq_num(array):
    new_unic_list = set(array)
    res_array = list(new_unic_list)
    return res_array


try:
    list_size = int(input("Введите размер последовательноси: "))
    start_list = create_list(list_size)
    print('Исходная последовательность: ')
    print(' '.join(map(str, start_list)))

    result_list = show_uniq_num(start_list)
    print("Список неповторяющихся элементвов в исходной последовательности: ")
    print(' '.join(map(str, result_list)))
except:
    print('Введите число')
