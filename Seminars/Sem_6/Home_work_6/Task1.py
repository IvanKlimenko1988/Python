# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def show_arithmetic_progression(start_num, range_num, size):
    list_result = []
    list_result.append(start_num)
    for i in range(1, size):
        start_num += range_num
        list_result.append(start_num)
    print(list_result)


a = int(input("--> Первый элемент: "))
b = int(input("--> Разность: "))
c = int(input("--> Количество элементов: "))
show_arithmetic_progression(a, b, c)
