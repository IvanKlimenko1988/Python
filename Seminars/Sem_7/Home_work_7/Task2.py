# Задание №2.
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у
# операции умножения.
# Ввод:
#
# print_operation_table(lambda x, y: x * y)
#
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36
def print_operation_table(operation, num_rows, num_columns):
    matrix = []
    for i in range(num_rows):
        temp = []
        for j in range(num_columns):
            temp.append(operation(i + 1, j + 1))
        matrix.append(temp)
        s = ""
        temp_s = ""
    for i in range(len(matrix[i])):
        s += temp_s + "\n"
        temp_s = ""
        for j in range(len(matrix[j])):
            temp_s += str(matrix[i][j]) + " "
    if temp_s != "":
        s += temp_s
    print(s)

num_rows = int(input("Введите количество сткрок: "))
num_columns = int(input("Введите количество столбцов: "))
operation = lambda x, y: x * y

print_operation_table(operation, num_rows, num_columns)

