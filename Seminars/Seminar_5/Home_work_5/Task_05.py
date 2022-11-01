# Дан список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1,  7]
#     [1, 5, 2, 3, 4,  1, 7, 8 , 15 , 1 ] => [1,  5]


# Рекомендация на каникулы - посмотреть библиотеку EasyGUI, БД SQLite.

# def create_list():
#     list = []
#     print('Заполните список числами!')
#     print('Чтобы закончить ввод, отправьте пустое значени!')
#     while(value := input('Введите число: ')) != '':
#         list.append(int(value))
#     return list

# def find_sequence(list):
#     min_value = min(list)
#     for i in range(len(list)):
#         if min_value in list:
#             min_value += 1
#         result = [min(list), min_value - 1]
#     return result

# try:
#     print('Найдем исключительные значения вашего списка!')
#     new_list = create_list()
#     print(f'Исходный списко: \n{new_list}')
#     result = find_sequence(new_list)
#     print(f'Максимальная последовательность: \n{result}')
# except ValueError as error:
#     print(f'Введите целове число! - {error}')



import re
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9


s = '5*x^3+2*x^2+6=0'

s1 = '7*x^2+6*x^1+3=0'

s = s.replace(' ', '')
s1 = s1.replace(' ', '')
s = s.replace('=0', '')
s1 = s1.replace('=0', '')

print(s)

print(s1)


result_x = re.findall(r'\S\^[1-9]', s)   #['x^3', 'x^2', 'x^4']
result_x1 = re.findall(r'\S\^[1-9]', s1)  

result_c1 = re.findall(r'\-?\d+', s1)
s = s.replace('x^3', '')
s = s.replace('x^2', '')
s1 = s1.replace('x^2', '')
s1 = s1.replace('x^1', '')

numbers = re.compile('-?\d+')
result_num = list(map(int, numbers.findall(s)))
result_num1 = list(map(int, numbers.findall(s1)))
print(result_num)
print(result_num1)


list_1 = list(zip(result_num, result_x))
list_2 = list(zip(result_num1, result_x1))
print(f'Первое уравнение: {list_1}')
print(f'Второе уравнение: {list_2}')

res_a = list_1[1][0] + list_2[0][0]
res_c = result_num[-1]+result_num1[-1]
print(res_c)

print(f'Результат: {list_1[0][0]}*{list_1[0][1]}+{res_a}*{list_1[1][1]}+{list_2[1][0]}*{list_2[1][1]}+{res_c}')


# def max_sequence(list1):
#     list1 = list(set(list1))
#     res_list = []
#     new_list = []
#     while len(list1) > 0:
#         min_value = min(list1)
#         list1.remove(min_value)
#         while True:
#             new_list.append(min_value)
#             min_value += 1
#             if not (min_value in list1):
#                 if len(new_list) > len(res_list):
#                     res_list = new_list.copy()
#                     new_list = []
#                 break
#             list1.remove(min_value)
#     return res_list

# def create_list(size):
#     lst = []
#     for i in range(size):
#         lst.append(int(input(f'Введите {i + 1} число: ')))
#     print(f'\nВаш список: {lst}')
#     return lst

# size = int(input('Введите размер списка: '))
# user_list = create_list(size)

# print(f'\nМаксимальная последовательность вашего списка: {max_sequence(user_list)}')

