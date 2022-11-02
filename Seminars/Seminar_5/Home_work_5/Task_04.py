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
    res_text = ''
    for i in range(len(text)):
        if 'x' == text[i]:
            count_x += 1
        if '^' == text[i]:
            count_d += 1
    if count_x != count_d:
        c_x = 0
        for i in range(len(text)):
            if text[i] == 'x':
                c_x += 1
            if text[i] == 'x' and count_x == c_x:
                res_text += 'x^1'
            else:
                res_text += text[i]
    else:
        return text
    return res_text


def max_deg(array):
    max_deg = []
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
        elif text[i] == 'x' and text[i - 1] == '-':
            continue
        elif text[i] == 'x' and text[i+1] == '^' and text[i-1] != '-':
            res_s += '1'
        elif text[i] == 'x' and text[i+1] == '^' and text[i - 1] == '+':
            res_s += '1'
        elif text[i] == 'x' and text[i+1] == '^':
            res_s += '1'
        else:
            res_s += text[i]
    return res_s


def create_ratio_list(text, max_deg):
    c_d = 0
    ratio_list = []
    st_1 = ''
    while max_deg > 0:
        for i in range(len(text)):
            if max_deg == 0:
                break
            if text[i] == '^' and text[i+1] == str(max_deg):
                c_d += 1
                if text[i+1] == str(max_deg):
                    ratio_list.append(''.join(map(str, numbers.findall(st_1))))
                    st_1 = ''
                    max_deg -= 1
            if text[i-1] == '^':
                st_1 = ''
                continue
            else:
                st_1 += text[i]
            if i == (len(text)-1):
                ratio_list.append('0')
                max_deg -= 1
                st_1 = ''
                break
    return ratio_list


def ratio_c(list_ch, str_s, list_ratio):
    if list_ch[-1] == '-':
        str_s = str_s.split('-')
        list_ratio.append(int(str_s[-1]) * (-1))
    elif list_ch[-1] == '+':
        str_s = str_s.split('+')
        list_ratio.append(int(str_s[-1]))
    return list_ratio


s = '5*x^3 + 2*x^2+6'
s1 = '7*x^2+6*x+3'

s = s.replace(' ', '')
s = s.replace('*', '')
s1 = s1.replace(' ', '')
s1 = s1.replace('*', '')

deg_s1 = re.findall(r'\S\^[1-9]', s)  # ['x^3', 'x^2']
deg_s2 = re.findall(r'\S\^[1-9]', s1)  # ['x^2', 'x^1']

s = add_deg_x(s)  # 5x^3+2x^2+6
s1 = add_deg_x(s1)  # 7x^2+6x^1+3 Добавляем степень x^1

max_deg_s1 = max_deg(deg_s1)  # Максимальная степень - 3
max_deg_s2 = max_deg(deg_s2)  # Максимальная степень - 2
result_max_deg = max(max_deg_s1, max_deg_s2)

numbers = re.compile('-?\d+')

s = start_poly(s)
s1 = start_poly(s1)

ratio_list_s1 = create_ratio_list(s, result_max_deg)
ratio_list_s2 = create_ratio_list(s1, result_max_deg)


sum_ch1 = re.findall(r'\D', s)
sum_ch2 = re.findall(r'\D', s1)


result_ratio_list_poly_1 = ratio_c(sum_ch1, s, ratio_list_s1)
result_ratio_list_poly_2 = ratio_c(sum_ch2, s1, ratio_list_s2)


result_1 = [int(item) for item in result_ratio_list_poly_1]
result_2 = [int(item) for item in result_ratio_list_poly_2]

res_list = [x + y for x, y in zip(result_1, result_2)]
print(res_list)



reseul_polynomial = ''
for i in range(len(res_list)):
    reseul_polynomial += f'{res_list[i]}'+'x^'+str(result_max_deg) + '+'
    result_max_deg -= 1
    if result_max_deg == 0:
        break
reseul_polynomial += str(res_list[-1])
print(reseul_polynomial)