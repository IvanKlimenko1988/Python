# Task002: Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

'''
print('Введите 5 чисел: ')
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

max = num1
if max < num2: max = num2
if max < num3: max = num3
if max < num4: max = num4
if max < num5: max = num5
print(f'Максимальное число = {max}')
'''
def create_list():
    numbers = []
    for i in range(5):
        value = int(input("Введите число: "))
        numbers.append(value)
    return numbers

def find_max(numbers):
    max = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max

result = create_list()
print(result)
max = find_max(result)
print(f'Максимальное число = {max}')
