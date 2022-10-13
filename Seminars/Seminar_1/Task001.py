# Task001:  Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет
'''
print('Введите два числа:', end=' ')
num1 = int(input())
num2 = int(input())
if num2 / num1 == num1 or num1 / num2 == num2: 
    print('Да')
else:
    print('Нет')
'''
'''
try:
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    if number1 ** 2 == number2:
        print(f'{number2} является квадратом числа {number1}')
    elif number2 ** 2 == number1:
        print(f'{number1} является квадратом числа {number2}')
    else:
        print('Ни одно из числе не является квадратом другого')
except:
    print('Введите целое число')
'''
try:
    numbers = []
    for i in range(5):
        numbers.append(int(input(f'Введите число {i+1}: ')))
        max_num = numbers[0]
        min_num = numbers[0]
        index_max = 0
        index_min = 0
        sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    if numbers[i] > max_num:
            max_num = numbers[i]
            index_max = i
    elif numbers[i] < min_num:
            min_num = numbers[i]
            index_min = i
            print('Максимальное число =', max_num, 'Индекс = ', index_max)
            print('Минимальное число =', min_num, 'Индекс = ', index_min)
            print('Среднее арифметическое = ', sum/len(numbers))
except:
    print('Введите целое число')

    