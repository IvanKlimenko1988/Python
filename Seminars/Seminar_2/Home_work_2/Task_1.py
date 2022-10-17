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




start_number = input('Введите вещественное или целое число: ')
print(start_number.isdigit())

float_digit = start_number.isdigit()
if float_digit == False:
    start_number = float(start_number)
    print(start_number)		
    while float_digit != True:
        start_number *= 10
        start_number = int(start_number)
        print(start_number)
        is_int = isinstance(start_number, int)
        if is_int == True:
            float_digit == True
            

print(float_digit)

