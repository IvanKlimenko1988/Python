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
s = s.replace('=0','')
ch_s = '-x'

if ch_s in s:
    s = s.replace(ch_s, '-1')
  
result = list(map(int, numbers.findall(s)))
print(result)



# 6*x^2+5*x+6=0
# x^2+5*x+6=0
# x^2+9*x=0
# x^2=0
# x^2+x=0
# 2*x^2=0
# 2*x^2+2=0

len_str = len(s)
if s.count('0*x^2', 0, len_str-2) or s.count('0x^2', 0, len_str-2):
    print("Уравнение не имеет решения, а = 0")
    exit()



ch_x = 'x'
ch_min = '-'
ch_plus = '+'
ch_deg = '^2'
ch_mul = '*x'







# print(s)

# s_len = len(s)
# i = 0

# abc =[]
# while i < s_len:

#     if s[i].isdigit():
#         abc.append(int(s[i]))
#         i += 1
#     elif s[i] == ch_min:
#         abc.append(int(s[i+1])*(-1))
#         i += 2
#     else:
#         i += 1

# i = 0
# abc_len = len(abc)

# print(abc)




















# s.split(' ') #: разбивает строку на подстроки в зависимости от разделителя
# ========================================================================================
# if s[0] == '0':
#     print("Уравнение не имеет решения, а = 0")
#     exit()
# print(s)
# print(len(s))
# sub = 'x'
# kf=s.count(sub)
# sub_1 = '+'
# kp = s.count(sub_1)
# sub_2 = '-'
# km = s.count(sub_2)
# print(km)


# min = '-'

# kof = []
# kof_dlina = len(kof)
# dlina = len(s)
# i = 0
# # for i in range(len(s)-2):
# while i < dlina-2:
#     if s[i] == '^':
#         i += 2
#         continue
#     elif s[i] == min:
#         if s[i+1] == "x":
#             kof.append(-1)
#         elif s[i+1] != "x":
#             kof.append(int(s[i+1])*(-1))
#             i += 1
#     # elif s[i] == "x" and s[i-1] == '-':
#     #     kof.append(1)
#     elif s[i] == "x" and s[i+1] == '^':
#         if s[0].isdigit():
#             i += 1
#             continue
#         if s[0] == '-':
#             i += 1
#             continue

        
#         else:
#             kof.append(1)
#     elif s[i] == "+" and s[i+1] == 'x':
#         kof.append(1)

#     elif s[i].isdigit():
#         kof.append(int(s[i]))
#     i += 1


# print(kof)
# str_1 = ''.join(map(str, kof))
# print(str_1)
# dlina_str_1 = len(str_1)
# print(len(kof))
# ----------------------------------------------------------------------
# if dlina_str_1 == 4:
#     kof.remove(1)
# else:
#     kof.append(0)

# if dlina_str_1 == 1:
#     kof.append(0)
#     kof.append(0)
# ===================================================================
# if kf == 2 and kp == 1:
#     kof.append(0)
# if kf == 1 and kp == 0 and km == 0:
#     kof.append(0)
#     kof.append(0)
# if kf == 1 and kp > 0 or km > 0:
#     kof.append(0)
#     temp = kof[1]
#     kof[1] = kof[-1]
#     kof[-1] = temp
# --------------------------------------------------------------------
# if kf == 1:
#     temp = kof[1]
#     kof[1] = kof[-1]
#     kof[-1] = temp

# if dlina_str_1 == 2:
#     kof.append(0)

# if len(kof) == 4:
#     kof.remove(kof[-1])
# ====================================================
# print(len(kof))
# print(kof)
# ---------------------------------------------------


# n = 0
# num = 0
# index_minus =[]
# index_num = []
# num_list = []
# while n < len(s):
#     if s[n] =='-':
#         if s[n+1] == 'x':
#             index_minus.append(n)
#             num_list.append(-1)
#             n += 1
#             continue
#         else:
#             index_minus.append(n)
#             num_list.append(int(s[n]) * (-1))
#             n += 1
#             continue

#     elif s[n].isdigit():
#         num += 1
#         index_num.append(n)
#         num_list.append(int(s[n]))
#         n += 1
#     else:
#         n += 1

# print(num)
# print(index_num)
# print(num_list)


# n = 0
# num = 0
# index_minus =[]
# index_num = []
# num_list = []
# while n < len(s):
#     if s[n] =='-':
#         index_minus.append(n)
#         num_list.append(int(s[n+1]) * (-1))
#         n += 2
#         continue

#     if s[n].isdigit():
#         num += 1
#         index_num.append(n)
#         num_list.append(int(s[n]))
#         n += 1
#     else:
#         n += 1

# print(num)
# print(index_num)
# print(num_list)


# # D = b**2 − 4ac.
# if num_list[0] == 2:
#     a = 1
#     b = num_list[1]
#     c = num_list[2]
# elif
# else:
#     a = num_list[0]
#     b = num_list[2]
#     c = num_list[3]

# D = b**2 - 4*a*c
# print(D)

# if D < 0:
#     print('Если D < 0, корней нет')
#     exit()
# elif D == 0:
#     print('Если D = 0, есть ровно один корень')
#     x1 = (-b + D**0.5)/2*a
#     print(x1)
# elif D > 0:
#     print('Если D > 0, корней будет два')
#     x1 = (-b + D**0.5)/2*a
#     x2 = (-b - D**0.5)/2*a
#     print(x1, x2)


# print(''.join(map(str, s)))


# for i in range(len(str_3)):
#     print(ord(str_3[i]))
