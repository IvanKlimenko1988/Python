# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def create_list(size):
    list_result = [] * size
    for i in range(size):
        list_result.append(int(input("Введите элемент массива: ")))
    return list_result


def show_index_range(list: list, start_range: int, end_range: int):
    index_list = []
    for i in range(len(list)):
        if end_range >= list[i] >= start_range:
            index_list.append(i)
    print(index_list)


start_list = create_list(5)

start_range = int(input("Введите начало диапазона: "))
end_range = int(input("Введите конец диапазона: "))

show_index_range(start_list, start_range, end_range)
