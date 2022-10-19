#  Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# def sum_digits(number):
#     substring = '.'
#     if substring in number:     # Поиск точки в строке
#         length = len(number)
#         num = float(number)
#         current = 0
#         while current < length - 1:
#             num *= 10
#             current += 1
#         current = num
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {number} = {round(sum)}')
#     else:
#         num = int(number)
#         current = num
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {number} = {sum}')


# try:
#     start_number = input('Введите вещественное или целое число: ')
#     sum_digits(start_number)
# except:
#     print('Введите вещественное число используя "." или целое число!')

##################################

# def sum_digits(number):
#     float_digit = start_number.isdigit()
#     if float_digit == False:
#         new_num = int(start_number.replace('.',''))
#         print(start_number)
#         current = new_num
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {start_number} = {sum}')
#     else:
#         current = int(start_number)
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {start_number} = {sum}')

# try:
#     start_number = input('Введите вещественное или целое число: ')
#     sum_digits(start_number)
# except:
#     print('Введите вещественное число используя "." или целое число!')


# def sum_digits(number):
#     float_digit = start_number.isdigit()
#     if float_digit == False:
#         new_num = float(start_number.replace('.',''))
#         print(start_number)
#         current = new_num
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {start_number} = {sum}')
#     else:
#         current = int(start_number)
#         sum = 0
#         while current > 0:
#             sum += current % 10
#             current //= 10
#         print(f'Сумма цифр числа {start_number} = {sum}')

# try:
#     start_number = input('Введите вещественное или целое число: ')
#     sum_digits(start_number)
# except:
#     print('Введите вещественное число используя "." или целое число!')

from fractions import*


# f_one = fractions.Fraction(3, 5) 
# f_two = fractions.Fraction(4, 9) 
# print('{} + {} = {}'.format(f_one, f_two, f_one + f_two))
# print('{} - {} = {}'.format(f_one, f_two, f_one - f_two)) 
# print('{} * {} = {}'.format(f_one, f_two, f_one * f_two)) 
# print('{} / {} = {}'.format(f_one, f_two, f_one / f_two))

num = 0.56
n1 = int(num)
n2 = num - n1
print(n1)
print(Fraction(n2))
fract = Fraction(n2)
Fraction(n2)
print(fract.numerator)
print(fract.denominator)
# fract = fractions.Fraction(5,6)
# print("Numerator: {}".format(fract.numerator)) 
# print("Denominator: {}".format(fract.denominator))
# a = fract.numerator
# b = fract.denominator
# print(a + b)
# print('{}'.format(fract))
