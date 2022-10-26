# Найдите корни квадратного уравнения, уравнение вводит через строку пользователь.
# например, 6*x^2+5*x+6=0 . Само собой, уравнение может и не иметь решения.
# Предусмотреть все варианты, сделать обработку исключений.

# Квадратное уравнение — это уравнение вида ax2 + bx + c = 0,
# где коэффициенты a, b и c — произвольные числа, причем a ≠ 0.

# Не имеют корней;
# Имеют ровно один корень;
# Имеют два различных корня.

# Пусть дано квадратное уравнение ax2 + bx + c = 0.
# Тогда дискриминант — это просто число D = b2 − 4ac.

# Если D < 0, корней нет;
# Если D = 0, есть ровно один корень;
# Если D > 0, корней будет два.

import re
print('Программа для решения квадратных уравнений')
numbers = re.compile('-?\d+')
s = ''.join(input("Введите элементы уравнение, например: '6*x^2+5*x+6=0': ").split()).lower()
s = s.replace('^2', '')
s = s.replace('=0', '')

sum_min = 0
result = list(map(int, numbers.findall(s)))

sum_min = 0
sum_plus = 0

for i in range(len(s)):
    sum_x = s.count('x')
    sum_min = s.count('-')
    sum_plus = s.count('+')

ch_minus = 'x-x' 
ch_plus = 'x+x' 
ch_xmul = '*x'

if sum_x == 2 and sum_min == 0 and sum_plus == 2 and len(result) == 3:
    print(result)
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
elif sum_x == 2 and sum_min == 1 and sum_plus == 0 and len(result) == 1 and ch_minus in s:
    result.append(-1)
    result.append(0)
elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 1 and ch_minus in s:
    result.append(1)
    result.append(0)  
    temp = result[1]
    result[1] = result[-1]
    result[-1] = temp
    result.reverse() 
elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 1 and ch_plus in s:
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
elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 1 and ch_xmul in s:
    result.append(0)
    result.append(1)
    temp = result[0]
    result[0] = result[1]
    result[1] = temp
    result.reverse()  
elif sum_x == 2 and sum_min == 1 and sum_plus == 0 and len(result) == 1 and ch_xmul in s:
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
elif sum_x == 1 and sum_min == 1 and sum_plus == 0 and len(result) == 1:
    print("Уравнение имеет один корень x = 0")
elif sum_x == 1 and sum_min == 0 and sum_plus == 0 and len(result) == 1:
    print("Уравнение имеет один корень x = 0")

if sum_x == 0 and len(result) == 1:
    print("Уравнение имеет один корень x = 0")
        
if sum_x == 1 and len(result) == 0:    
    print("Уравнение имеет один корень x = 0")

len_str = len(s)
if s.count('0*x^2', 0, len_str-2) or s.count('0x^2', 0, len_str-2):
    print("Уравнение не имеет решения, а = 0")
    exit()

# ----------------------------------------------
# Нашли все возможные коэффициенты a, b и с!!
# ----------------------------------------------

a = result[0]
b = result[1]
c = result[2]
x1 = 0
x2 = 0

# ---------------------------------------------------
# Неполные квадратные уравнения, если b = 0 или c = 0
# ---------------------------------------------------

# Если b = 0
if b == 0:
    if -c / a >= 0: # Если выполняется это условие,корней будет два.
        x1 = -(-c / a)**0.5
        x2 = (-c / a)**0.5
        print('Ответ:')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
        exit()

    elif -c / a < 0: # Корней нет.
        print('Ответ: корней нет')
        exit()

elif c == 0:
        # Если с = 0, корней будет два.
        x1 = 0
        x2 = -b / a
        print('Ответ:')
        print(f'x1 = {x1}')
        print(f'x2 = {x2}')
        exit()

discriminant = b**2 - 4 * a * c
print(f'D = {discriminant}')

if discriminant < 0: # Если D < 0, корней нет
    print('D < 0')
    print('Ответ: корней нет')
    exit()

elif discriminant == 0: # Если D = 0, есть ровно один корень
    x1 = (-b + discriminant**0.5) / 2 * a
    print('D = 0, есть ровно один корень')
    print(f'Ответ: x1 = {x1}')
    exit()

elif discriminant > 0: #Если D > 0, корней будет два.
    x1 = (-b + discriminant**0.5) / 2 * a
    x2 = (-b - discriminant**0.5) / 2 * a
    print('D > 0, корней будет два')
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
    exit()
