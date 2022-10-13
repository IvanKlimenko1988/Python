# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
 
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
 
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
 
# Обратите внимание, что на вход программе приходят вещественные числа.
 
# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!
 
# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0
# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5
try:
    print('Это простой калькутятор!')
    print('Он поддерживает операции: +, -, /, *, mod, pow, div, где')
    print('mod — это взятие остатка от деления')
    print('pow — возведение в степень')
    print('div — целочисленное деление')
    
    print('Введите первое число:', end=' ')
    number1 = float(input())
    print('Введите второе число:', end=' ')
    number2 = float(input())
    print('Введите операцию:', end=' ')
    operation = input()
    
    if operation == "+":
        print('Результат:', end=' ')
        print(number1 + number2)
    elif operation == "-":
        print('Результат:', end=' ')
        print(number1 - number2)
    elif operation == "*":
        print('Результат:', end=' ')
        print(number1 * number2)
    elif operation == 'pow':
        print('Результат:', end=' ')
        print(number1 ** number2)
    if operation == "div":
        if number2 == 0:
            print("Деление на 0!")
        else:
            print('Результат:', end=' ')
            print(number1 // number2)
    if operation == "/":
        if number2 == 0:
            print("Деление на 0!")
        else:
            print('Результат:', end=' ')
            print(number1 / number2)
    if operation == 'mod':
        if number2 == 0:
            print("Деление на 0!")
        else:
            print('Результат:', end=' ')
            print(number1 % number2)
except:
    print('Введите число или доступные операции')