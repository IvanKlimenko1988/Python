# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re

# """задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9"""

# def max_degree(poly):
#     list = poly.replace(' ', '').split('x')
#     degree = 0
#     check = 0
#     for i in list:
#         for l in range(len(i)):
#             if i[l] == '^':
#                 check = 1
#                 degree = int(i[l + 1])
#                 break
#         if check == 1:
#             check = 0
#             break
#     return degree

# def list_of_coefficients(poly1, degree):
#     list = poly1.split('+')
#     new_list = []
#     d = degree
#     i = 0
#     while d > 0:
#         if i < len(list):
#             if not 'x' in list[i]:
#                 new_list.append(0)
#             else:
#                 if list[i][0] == '-':
#                     if list[i][1].isdigit():
#                         temp = int(list[i][1]) * (-1)
#                     elif list[i][1] == 'x':
#                         temp = -1
#                 elif list[i][0].isdigit():
#                     temp = int(list[i][0])
#                 elif list[i][0] == 'x':
#                     temp = 1
#                 for l in range(len(list[i])):
#                     if list[i][l] == 'x':
#                         if ('^' in list[i]) and (list[i][l + 1] == '^'):
#                             if list[i][l + 2] == str(d):
#                                 new_list.append(temp)
#                                 i += 1
#                             else:
#                                 new_list.append(0)
#                             break
#                         else:
#                             if '1' == str(d):
#                                 new_list.append(temp)
#                                 i += 1
#                             else:
#                                 new_list.append(0)
#                             break
#         else:
#             new_list.append(0)
#             new_list.append(0)
#         d -= 1
#     for j in list:
#         if not 'x' in j:
#             new_list.append(int(j))
#     return new_list

# def list_to_polynomial(list1):
#     res = ''
#     degree = len(list1) - 1
#     for i in list1:
#         if i != 0:
#             if degree == 1:
#                 res += f'{str(i)}*x^{degree} + '
#                 degree -= 1
#             elif degree == 0:
#                 res += f'{str(i)}'
#             else:
#                 res += f'{str(i)}*x^{degree} + '
#                 degree -= 1
#         else:
#             degree -= 1

#     res = res.replace('+ -', '- ')
#     print(res)


# polynomial_first = ' 5*х^4 - 2*x^2 - 6'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')
# polynomial_second = ' 7*x^2 - x - 3'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')

# print(polynomial_first)
# print(polynomial_second)
# degree1 = max_degree(polynomial_first)
# degree2 = max_degree(polynomial_second)
# maximum_degree = max(degree1, degree2)
# list1 = list_of_coefficients(polynomial_first, maximum_degree)
# list2 = list_of_coefficients(polynomial_second, maximum_degree)
# res_list = [x + y for x, y in zip(list1, list2)]
# list_to_polynomial(res_list)

# """задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9"""





# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
def add_deg_x(text):
    count_x = 0
    count_d = 0
    res_text =''
    for i in range(len(text)):
        if 'x' == text[i]:
            count_x +=1
        if '^' == text[i]:
            count_d +=1
    if count_x != count_d:
        c_x = 0
        for i in range(len(text)):
            if text[i] == 'x':
                c_x +=1
            if text[i] == 'x' and count_x == c_x:
                res_text += 'x^1'
            else:
                res_text +=text[i]              
    else:
        return text
    return res_text

def max_deg(array):
    max_deg =[]
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j].isdigit():
                max_deg.append(array[i][j])
    max_deg = int(max(max_deg))
    return max_deg

def start_poly(text):
    res_s = ''
    for i in range(len(text)):
        if text[i] == '-' and text[i+1] == 'x':
            res_s += '-1'
            continue
        elif text[i].isdigit():
            res_s += text[i]
        elif text[i] == 'x' and text[i-1].isdigit():
            continue
        elif text[i] == 'x' and text[i -1] == '-':
            continue
        elif text[i] == 'x' and text[i+1] =='^' and text[i-1] != '-':
            res_s += '1'
        elif text[i] == 'x' and text[i+1] =='^' and text[i -1] == '+':
            res_s += '1'
        elif text[i] == 'x' and text[i+1] =='^':
            res_s += '1'
        else:
            res_s += text[i]
    return res_s



s = '5*x^3 + 2*x^2+ 6'
s1 = '7*x^2+6*x+3'

s = s.replace(' ', '')
s = s.replace('*', '')
s1 = s1.replace(' ', '')
s1 = s1.replace('*', '')

deg_s1 = re.findall(r'\S\^[1-9]', s)   #['x^3', 'x^2']
deg_s2 = re.findall(r'\S\^[1-9]', s1)  #['x^2', 'x^1']

s = add_deg_x(s)   #5x^3+2x^2+6 
s1 = add_deg_x(s1) #7x^2+6x^1+3 Добавляем степень x^1 
  
max_deg_s1 = max_deg(deg_s1) # Максимальная степень - 3
max_deg_s2 = max_deg(deg_s2) # Максимальная степень - 2
result_max_deg = max(max_deg_s1,max_deg_s2)
print(result_max_deg)
# print(max_deg_s1)
# print(max_deg_s2)

result_c1 = re.findall(r'\-?\d+', s1)
# s = s.replace('x^3', '')
# s = s.replace('x^2', '')
# text = s1.replace('x^2', '')
# text = s1.replace('x^1', '')

numbers = re.compile('-?\d+')
result_num = list(map(int, numbers.findall(s)))
result_num1 = list(map(int, numbers.findall(s1)))
print(result_num)
print(result_num1)


s = start_poly(s)
s1 = start_poly(s1)
print(s)
print(s1)

# while result_max_deg > 0:



# list_1 = list(zip(result_num, deg_s1))
# list_2 = list(zip(result_num1, deg_s2))
# print(f'Первое уравнение: {list_1}')
# print(f'Второе уравнение: {list_2}')

# res_a = list_1[1][0] + list_2[0][0]
# res_c = result_num[-1]+result_num1[-1]
# print(res_c)

# print(f'Результат: {list_1[0][0]}*{list_1[0][1]}+{res_a}*{list_1[1][1]}+{list_2[1][0]}*{list_2[1][1]}+{res_c}')