# 2. Требудется найти в массиве A[1...N] самый большой по величене
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N - количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последня строка содержит число X.

# input
# 5
# 1 2 3 4 5
# 6
# -> 5

# n = int(input("Введите количество элементов в массиве: "))
# start_list = [] * n
# numbers = 0
#
# while numbers < n:
#     start_list.append(int(input(f"Введите {numbers + 1} элемент массива: ")))
#     numbers += 1
start_list = [10, 2, 15, 43, 4]
x = int(input("Введите искомый элемент Х: "))

check = False
max_val = 0
for i in range(len(start_list)):
    if start_list[i] == x:
        max_val = start_list[i]
        check = True
    elif (max_val < start_list[i]) & (check == False):
        max_val = start_list[i]


print(max_val)

