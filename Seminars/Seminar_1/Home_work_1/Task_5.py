# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

list = [[1, 4, 7, 2], [5, 9, 10, 3]]

row = int(input('Введите количество строк'))
columns = int(input('Введите количество столбцов'))

for i in range(row):
    for j in range(columns):
        print(list[i][j], end=' ')


