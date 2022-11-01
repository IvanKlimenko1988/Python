# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
import re

"""задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9"""

def max_degree(poly):
    list = poly.replace(' ', '').split('x')
    degree = 0
    check = 0
    for i in list:
        for l in range(len(i)):
            if i[l] == '^':
                check = 1
                degree = int(i[l + 1])
                break
        if check == 1:
            check = 0
            break
    return degree

def list_of_coefficients(poly1, degree):
    list = poly1.split('+')
    new_list = []
    d = degree
    i = 0
    while d > 0:
        if i < len(list):
            if not 'x' in list[i]:
                new_list.append(0)
            else:
                if list[i][0] == '-':
                    if list[i][1].isdigit():
                        temp = int(list[i][1]) * (-1)
                    elif list[i][1] == 'x':
                        temp = -1
                elif list[i][0].isdigit():
                    temp = int(list[i][0])
                elif list[i][0] == 'x':
                    temp = 1
                for l in range(len(list[i])):
                    if list[i][l] == 'x':
                        if ('^' in list[i]) and (list[i][l + 1] == '^'):
                            if list[i][l + 2] == str(d):
                                new_list.append(temp)
                                i += 1
                            else:
                                new_list.append(0)
                            break
                        else:
                            if '1' == str(d):
                                new_list.append(temp)
                                i += 1
                            else:
                                new_list.append(0)
                            break
        else:
            new_list.append(0)
            new_list.append(0)
        d -= 1
    for j in list:
        if not 'x' in j:
            new_list.append(int(j))
    return new_list

def list_to_polynomial(list1):
    res = ''
    degree = len(list1) - 1
    for i in list1:
        if i != 0:
            if degree == 1:
                res += f'{str(i)}*x^{degree} + '
                degree -= 1
            elif degree == 0:
                res += f'{str(i)}'
            else:
                res += f'{str(i)}*x^{degree} + '
                degree -= 1
        else:
            degree -= 1

    res = res.replace('+ -', '- ')
    print(res)


polynomial_first = ' 5*x^3 + 2*x^2 + 6'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')
polynomial_second = ' 7*x^2 - x + 3'.replace('х', 'x').replace(' ', '').replace('*', '').replace('-','+-')
degree1 = max_degree(polynomial_first)
degree2 = max_degree(polynomial_second)
maximum_degree = max(degree1, degree2)
list1 = list_of_coefficients(polynomial_first, maximum_degree)
list2 = list_of_coefficients(polynomial_second, maximum_degree)
res_list = [x + y for x, y in zip(list1, list2)]
list_to_polynomial(res_list)

"""задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9"""
