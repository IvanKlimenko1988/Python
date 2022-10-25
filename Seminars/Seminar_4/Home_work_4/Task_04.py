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


numbers = re.compile('-?\d+')
s = ''.join(input("Введите элементы уравнение через пробел: ").split()).lower()
s = s.replace('^2', '')
s = s.replace('=0', '')
# ch_s = '-x'

# if ch_s in s:
#     s = s.replace(ch_s, '-1')

sum_min = 0
result = list(map(int, numbers.findall(s)))
print(result)


sum_min = 0
sum_plus = 0
for i in range(len(s)):
    sum_x = s.count('x')
    sum_min = s.count('-')
    sum_plus = s.count('+')
print(f"'x' = {sum_x}")
print(f"'-' = {sum_min}")
print(f"'+' = {sum_plus}")


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
elif sum_x == 2 and sum_min == 1 and sum_plus == 1 and len(result) == 0:
    result.append(-1)
    result.append(1)
    result.append(0)    
elif sum_x == 2 and sum_min == 1 and sum_plus == 0 and len(result) == 1:
    result.append(1)
    result.append(0)
    temp = result[0]
    result[0] = result[1]
    result[1] = temp
elif sum_x == 2 and sum_min == 1 and sum_plus == 2 and len(result) == 2:
    result.append(-1)
    result.reverse()  
    temp = result[1]
    result[1] = result[-1]
    result[-1] = temp
elif sum_x == 1 and sum_min == 1 and sum_plus == 1 and len(result) == 1:
    result.append(-1)
    result.append(0) 
    temp = result[0]
    result[0] = result[-1]
    result[-1] = temp
    temp = result[0]
    result[0] = result[1]
    result[1] = temp
elif sum_x == 1 and sum_min == 2 and sum_plus == 0 and len(result) == 1:
    result.append(-1)
    result.append(0) 
    temp = result[0]
    result[0] = result[-1]
    result[-1] = temp
    temp = result[0]
    result[0] = result[1]
    result[1] = temp
elif sum_x == 2 and sum_min == 0 and sum_plus == 2:
    result.append(1)
    result.reverse()  
    temp = result[1]
    result[1] = result[-1]
    result[-1] = temp
elif sum_x == 2 and sum_min == 0 and sum_plus == 1 and len(result) == 0:
    result.append(1)
    result.append(1)
    result.append(0)
elif sum_x == 2 and sum_min == 0 and sum_plus == 1:
    result.append(1)
    result.append(0)
    temp = result[0]
    result[0] = result[1]
    result[1] = temp
elif sum_x == 2 and sum_min == 2 and sum_plus == 0 and len(result) == 2:
    result.append(1)
    result.reverse()  
    temp = result[1]
    result[1] = result[-1]
    result[-1] = temp
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

for i in range(len(s)):
    print(s[i], end= '')
print()
    
    
if sum_x == 0 and len(result) == 1:
    print("Уравнение имеет один корень x = 0")    
if sum_x == 1 and len(result) == 0:    
    print("Уравнение имеет один корень x = 0")

print(result)
# 6*x^2+5*x+6=0
# x^2+5*x+6=0
# x^2+9*x=0

# x^2+x=0

# 2*x^2+2=0

len_str = len(s)
if s.count('0*x^2', 0, len_str-2) or s.count('0x^2', 0, len_str-2):
    print("Уравнение не имеет решения, а = 0")
    exit()
