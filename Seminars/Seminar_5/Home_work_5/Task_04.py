# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

import re


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
    a = len(text)
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
            if i == (len(text)-2):
                ratio_list.append('0')
                max_deg -= 1
                st_1 = ''
                break
    for i in range(len(ratio_list)):
        if ratio_list[i] == '':
            ratio_list[i] = '1'
    return ratio_list


def ratio_c(list_ch, str_s, list_ratio):
    if list_ch[-1] == '-':
        str_s = str_s.split('-')
        list_ratio.append(int(str_s[-1]) * (-1))
    elif list_ch[-1] == '+':
        str_s = str_s.split('+')
        list_ratio.append(int(str_s[-1]))
    return list_ratio


def show_result_polynomual(res_list, result_max_deg):
    reseul_polynomial = ''

    for i in range(len(res_list)):
        reseul_polynomial += f'{res_list[i]}'+'*x^'+str(result_max_deg) + '+'
        result_max_deg -= 1
        if result_max_deg == 0:
            break
    reseul_polynomial += str(res_list[-1])
    for i in range(len(reseul_polynomial)-1):
        if reseul_polynomial[i] == '+' and reseul_polynomial[i+1] == '-':
            reseul_polynomial = reseul_polynomial.replace('+-', '-')
        elif reseul_polynomial[i] == '+' and reseul_polynomial[i+1] == '0':
            reseul_polynomial = reseul_polynomial.replace('+0', '')
    ch = '1*'
    if ch in reseul_polynomial:
        reseul_polynomial = reseul_polynomial.replace('1*', '')
    return reseul_polynomial


# 52x^3-2x^2-x+3 - удаляем лишние пробелы и знаки
s = '52*x^3 - 2*x^2 - x + 3'.replace(' ', '').replace('*', '')
s1 = 'x^2+6*x'.replace(' ', '').replace('*', '')               # x^2+6x

deg_s1 = re.findall(r'\S\^[1-9]', s)  # ['x^3', 'x^2']
deg_s2 = re.findall(r'\S\^[1-9]', s1)  # ['x^2', 'x^1']

s = add_deg_x(s)  # 5x^3+2x^2+6
s1 = add_deg_x(s1)  # 7x^2+6x^1+3 Добавляем степень x^1

max_deg_s1 = max_deg(deg_s1)  # Максимальная степень - 3
max_deg_s2 = max_deg(deg_s2)  # Максимальная степень - 2
result_max_deg = max(max_deg_s1, max_deg_s2)

numbers = re.compile('-?\d+')  # Компилируем шаблон для поиска чисел в строке

s = start_poly(s)  # 52^3-2^2-1^1+3 -получаем строку со степенями
s1 = start_poly(s1)  # ^2+6^1

ratio_list_s1 = create_ratio_list(s, result_max_deg)   # ['52', '-2', '-1'] - Получаем коэфициенты перед 'X'
ratio_list_s2 = create_ratio_list(s1, result_max_deg)  # ['0', '1', '6', '0']

sum_ch1 = re.findall(r'\D', s)  # ['^', '-', '^', '-', '^', '+'] - Получаем список знаков, нас интересует последний знак
sum_ch2 = re.findall(r'\D', s1) # ['^', '+', '^']

result_ratio_list_poly_1 = ratio_c(sum_ch1, s, ratio_list_s1)
result_ratio_list_poly_2 = ratio_c(sum_ch2, s1, ratio_list_s2)

result_1 = [int(item) for item in result_ratio_list_poly_1] # [52, -2, -1, 3] - Получаем итоговые значения в каждом многочлене
result_2 = [int(item) for item in result_ratio_list_poly_2] # [0, 1, 6, 0]

res_list = [x + y for x, y in zip(result_1, result_2)]      # [52, -1, 5, 3] - Получаем сумму двух коэффициентов многочленов

show_result = show_result_polynomual(res_list, result_max_deg) # 52*x^3-x^2+5*x^1+3 - результат

print(show_result) 
