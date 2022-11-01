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

s1 = '7*x^2+6*x+3=0'

s = s.replace(' ', '')
s1 = s1.replace(' ', '')
s = s.replace('=0', '')
s1 = s1.replace('=0', '')

print(s)

print(s1)


result_x = re.findall(r'\S\^[1-9]', s)   #['x^3', 'x^2', 'x^4']
result_x1 = re.findall(r'\S\^[1-9]', s1)   #['x^3', 'x^2', 'x^4']
# result_x1 = re.findall(r'x[^+]', s1)   #['x^3', 'x^2', 'x^4']


result_c1 = re.findall(r'\-?\d+', s1)
s = s.replace('x^3', '')
s = s.replace('x^2', '')
s1 = s1.replace('x^2', '')

numbers = re.compile('-?\d+')
result_num = list(map(int, numbers.findall(s)))
result_num1 = list(map(int, numbers.findall(s1)))




# print(result_x)
# print(result_x1)





# print(result_num)
# print(result_num1)


list_1 = list(zip(result_num, result_x))
list_2 = list(zip(result_num1, result_x1))
print(f'Первое уравнение: {list_1}')
print(f'Второе уравнение: {list_2}')

# c = int(result_c[-1])
# c1 = int(result_c1[-1])
# print(f'Свободный член: {c}')
# print(f'Свободный член: {c1}')


# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
res_a = list_1[1][0] + list_2[0][0]

print(f'Результат: {list_1[0][0]}*{list_1[0][1]}+{res_a}*{list_1[1][1]}')













# result_x2 = re.findall(r'\^.', s)
# result_x2 = re.findall(r'\d+.x.', s)
# result_x3 = re.findall(r'\*',s)




# result = re.search(r'x.3', s) #<re.Match object; span=(2, 5), match='x^3'>
# result = re.search(r'\d', s) #<re.Match object; span=(0, 1), match='5'>
# result = re.search(r'\D', s) #<re.Match object; span=(1, 2), match='*'>
# result = re.search(r'\d*', s) #<re.Match object; span=(0, 3), match='525'>

# result = re.search(r'\d{1,1}', s) #<re.Match object; span=(0, 3), match='525'>