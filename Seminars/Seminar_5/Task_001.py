from ast import comprehension


# Lambda - для создания маленьких ананимных функций
# map - применяет функцию к списку или словарю, возвращает объект
# Filter - применяет логическую функцию к списку или словарю, возвращает элименты,
# которые удовлетворяют условию
# Zip - создаёт кортежи из элементов словарей или списков
# List comprehension - удобная генерация списков.


# add = lambda x, y: x + y  #анонимная маленькая функция
# print(add(2, 5))   # add = 7

# def multiply2(x):
#     return x * 2

# print(list(map(multiply2, [1, 2, 3, 4]))) #  К каждому элементу списка выполнилась функция [2, 4, 6, 8]

# dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

# res = list(filter(lambda x: x['name'] == 'python', dict_a)) #[{'name': 'python', 'points': 10}]

# print(res)

# a = [10, 20, 30, 40]
# b = ['a', 'b', 'c', 'd', 'e']

# for i, j in zip(a, b): 
#     print(i, j)                 #10 a, 20 b, 30 c, 40 d

# spisok = [16, 46, 26, 36]

# for i in enumerate(spisok, start=1):
#     print(i)                    #(1, 16) (2, 46) (3, 26) (4, 36)


# squares = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 
# odds = [x for x in range(10) if x % 2 != 0] # [1, 3, 5, 7, 9]

# print(squares)

# print(odds)

# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность. Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# [1, 2, 8, 1 2, 3, 4, 1, 7] => [1, 4]



def create_list():
    list = []
    print('Заполните список числами!')
    print('Чтобы закончить ввод, отправьте пустое значени!')
    while(value := input('Введите число: ')) != '':
        list.append(int(value))
    return list

def find_sequence(list):
    min_value = min(list)
    for i in range(len(list)):
        if min_value in list:
            min_value += 1
        result = [min(list), min_value - 1]
    return result

try:
    print('Найдем исключительные значения вашего списка!')
    new_list = create_list()
    print(f'Исходный списко: \n{new_list}')
    result = find_sequence(new_list)
    print(f'Максимальная последовательность: \n{result}')
except ValueError as error:
    print(f'Введите целове число! - {error}')