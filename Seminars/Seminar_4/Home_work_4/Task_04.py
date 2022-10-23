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


s= input("Введите элементы уравнение через пробел: ").split()
# s = ['6', '*', 'x', '^', '2', '+', '5', '*', 'x', '+', '6', '=', '0']


if s[0] == '0':
    print("Уравнение не имеет решения, а = 0")
    exit()

print(''.join(map(str, s)))

s.remove('=')
s.remove('0')

n = 0
num = 0
index_minus =[]
index_num = []
num_list = []
while n < len(s):
    if s[n] =='-':
        index_minus.append(n)
        num_list.append(int(s[n+1]) * (-1))
        n += 2
        continue

    elif s[n].isdigit():
        num += 1
        index_num.append(n)
        num_list.append(int(s[n]))
        n += 1
    else:
        n += 1
    
print(num)
print(index_num)
print(num_list)






























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


# D = b**2 − 4ac.

a = num_list[0]
b = num_list[2]
c = num_list[3]

D = b**2 - 4*a*c
print(D)

if D < 0:
    print('Если D < 0, корней нет')
    exit()
elif D == 0:
    print('Если D = 0, есть ровно один корень')
    x1 = (-b + D**0.5)/2*a
    print(x1)
elif D > 0:
    print('Если D > 0, корней будет два')
    x1 = (-b + D**0.5)/2*a
    x2 = (-b - D**0.5)/2*a
    print(x1, x2)


print(''.join(map(str, s)))


# for i in range(len(str_3)):
#     print(ord(str_3[i]))
