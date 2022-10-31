# Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
import re

def find_a_b_c(str):

    numbers = re.compile('-?\d+')
    # str = ''.join(input("Введите элементы уравнение, например: '6*x^2+5*x+6=0': ").split()).lower()
    str = str.replace('^2', '')
    str = str.replace('=0', '')
    str = str.replace('^3', '')

    result = list(map(int, numbers.findall(str)))
    print(result)
    sum_min = 0
    sum_plus = 0

    for i in range(len(str)):
        sum_x = str.count('x')
        sum_min = str.count('-')
        sum_plus = str.count('+')

    ch_minus = 'x-x' 
    ch_plus = 'x+x' 
    ch_xmul = '*x'

    if sum_x == 2 and sum_min == 0 and sum_plus == 2 and len(result) == 3:
        print(f'Коэффициенты : {result}')
    elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 2:
        result.append(1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 2 and sum_min == 3 and sum_plus == 0 and len(result) == 2:
        result.append(-1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 2 and sum_min == 2 and sum_plus == 1 and len(result) == 2:
        result.append(-1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 2 and sum_min == 2 and sum_plus == 0 and len(result) == 2:
        result.append(1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 2 and sum_min == 1 and sum_plus == 2 and len(result) == 2:
        result.append(-1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp 
    elif sum_x == 2 and sum_min == 1 and sum_plus == 0 and len(result) == 1 and ch_minus in str:
        result.append(-1)
        result.append(0)
    elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 1 and ch_minus in str:
        result.append(1)
        result.append(0)  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
        result.reverse() 
    elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 1 and ch_plus in str:
        result.append(1)
        result.append(0)  
    elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 1:
        result.append(1)
        result.append(1)  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
        result.reverse() 
    elif sum_x == 1 and sum_min == 1 and sum_plus == 1 and len(result) == 1:
        result.append(-1)
        result.append(0) 
        temp = result[0]
        result[0] = result[-1]
        result[-1] = temp
        temp = result[0]
        result[0] = result[1]
        result[1] = temp
    elif sum_x == 1 and sum_min == 1 and sum_plus == 0 and len(result) == 2:
        result.append(0) 
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 1 and sum_min == 2 and sum_plus == 0 and len(result) == 1:
        result.append(-1)
        result.append(0) 
        temp = result[0]
        result[0] = result[-1]
        result[-1] = temp
        temp = result[0]
        result[0] = result[1]
        result[1] = temp
    elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 0:
        result.append(-1)
        result.append(1)
        result.append(0)
    elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 0:
        result.append(1)
        result.append(1)
        result.append(0)
    elif sum_x == 2 and sum_min == 2 and sum_plus == 0 and len(result) == 0:
        result.append(-1)
        result.append(-1)
        result.append(0)
    elif sum_x == 2 and sum_min == 0 and sum_plus == 2:
        result.append(1)
        result.reverse()  
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 2:
        result.append(0)
    elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 1 and ch_xmul in str:
        result.append(0)
        result.append(1)
        temp = result[0]
        result[0] = result[1]
        result[1] = temp
        result.reverse()  
    elif sum_x == 2 and sum_min == 1 and sum_plus == 0 and len(result) == 1 and ch_xmul in str:
        result.append(1)
        result.append(0)
        temp = result[0]
        result[0] = result[1]
        result[1] = temp
    elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 1:
        result.append(1)
        result.append(0)
            
    elif sum_x == 2 and sum_min == 1 and sum_plus == 0:
        result.append(1)
        result.append(-1)
        result.append(0)
    elif sum_x == 1 and sum_min == 0 and sum_plus == 1:
        result.append(0)
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 1 and sum_min == 2 and sum_plus == 0:
        result.append(0)
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    elif sum_x == 1 and sum_min == 1 and sum_plus == 1:
        result.append(0)
        temp = result[1]
        result[1] = result[-1]
        result[-1] = temp
    return result[0] ,result[1], result[2]


try:
    print('Программа для решения квадратных уравнений')
    str = ''.join(input("Введите элементы уравнение, например: 'a*x^2+b*x+6=0': ").split()).lower()
    ch_x = 'x'
    ch_p ='+'
    ch_m = '-'
    if ch_x in str or ch_p in str or ch_m in str:
        a , b ,c = find_a_b_c(str)
        print(a)
        print(b)
        print(c)
        
    else:
        print('Программа завершила свою работу, неправильный ввод!')
except:
    print("Завершение программы")
