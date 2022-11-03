# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
# [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]


# Рекомендация на каникулы - посмотреть библиотеку EasyGUI, БД SQLite.

def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значени!')
    while (value := input('Введите число: ')) != '':
        list.append(int(value))
    return list


def find_sequence(list):
    list = set(list)
    max_list = []
    new_seq = []
    temp = []
    min_value = min(list)
    while len(list) > 0:
        if min_value in list:
            list.remove(min_value)
            temp.append(min_value)
            min_value += 1
            if len(list) == 0:
                if len(new_seq) > len(temp):
                    return new_seq
                else:
                    return temp
            else:
                continue
        if len(new_seq) > len(temp):
            temp.clear()
        else:
            new_seq = temp.copy()
            min_value += 1
            temp.clear()
        if min_value not in list:
            if len(max_list) > len(new_seq):
                new_seq.clear()
            else:
                max_list = new_seq.copy()
                min_value += 1
    return max_list


try:
    print('Найдем максимальную возрастающую последовательность списка!')
    new_list = create_list()
    print(f'Исходный список: \n{new_list}')
    result = find_sequence(new_list)
    print(f'Максимальная последовательность: \n[{result[0]}, {result[-1]}]')
except ValueError as error:
    print(f'Введите целове число! - {error}')
