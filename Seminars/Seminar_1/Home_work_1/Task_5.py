# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
array_num = []

for i in range(rows):
    temp = []
    for i in range(columns):
        temp.append(int(input('Введите значение элемента списка: ')))
    array_num.append(temp)
for i in array_num:
    print(i)

for run in range((rows*columns)-1):
    for i in range(rows):
        for j in range(columns-1-run):
            if array_num[i][j] > array_num[i][j+1]:
                array_num[i][j], array_num[i][j+1] = array_num[i][j+1], array_num[i][j]
print()

list_a = array_num[0]
list_b = array_num[1]
c = []
n = len(list_a) 
m = len(list_b)
i = 0
j = 0

while i < n and j < m:
    if list_a[i] <= list_b[j]:
        c.append(list_a[i])
        i += 1
    else:
        c.append(list_b[j])
        j += 1

c += list_a[i:] + list_b[j:]
print(c)

for arr in array_num:
    for el in arr:
        array_num[arr][el] = c[j]
        print(el, end=' ')
    print()

