# 2. Требудется найти в массиве A[1...N] самый большой по величене
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N - количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последня строка содержит число X.

# input
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
start_list = [] * n
numbers = 0

while numbers < n:
    start_list.append(int(input(f"Введите {numbers + 1} элемент массива: ")))
    numbers += 1

x = int(input("Введите искомый элемент Х: "))

print(f"Массив: {start_list}")

if x in start_list:
    print(f"Самое большое число к искомому {x} -> {x}")
else:
    list_result = []
    for i in range(len(start_list)):
        if x - start_list[i] < 0:
            list_result.append((x - start_list[i]) * (-1))
        else:
            list_result.append(x - start_list[i])
    min_diff = min(list_result)
    result_index = list_result.index(min_diff)
    print(f"Самое большое число к искомому {x} -> {start_list[result_index]}")


