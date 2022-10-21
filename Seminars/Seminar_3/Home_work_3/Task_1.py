# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def create_list(size):
    list = [0] * size
    for i in range(size):
        try:
            list[i] = int(input(f"Введите число {i+1}: "))
        except:
            print('Введите целое число')
    return list

def find_sum_list(list):
    sum = 0
    odd = []
    for elem in range(1,len(list_1)):
        if elem % 2 != 0:
            odd.append(list_1[elem])
            sum += list_1[elem]

    print('На нечётных позициях элементы:')
    for i in range(len(odd)):
        print(odd[i], end= ' ')
    print()
    return sum

try: 
    print('Найти сумму элементвов списка на нечётных позициях')   
    size = int(input('Введите размер списка: '))
    list_1 = create_list(size)
    print(list_1)
    result = find_sum_list(list_1)
    print(f'Ответ: {result}')
except:
    print('Введите числа!')
    
