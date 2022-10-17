# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(num):
    factorial = 1
    result_list = []
    for i in range(1, num + 1):
        factorial *= i
        result_list.append(factorial)
    return result_list


try:
    number = int(input('Введите целое число: '))
    print(f'{number}! = {factorial(number)}')
except:
    print('Введите целое число')
