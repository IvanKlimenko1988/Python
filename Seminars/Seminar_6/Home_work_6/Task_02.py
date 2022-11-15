# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:*
#     1+2*3 => 7;
#     (1+2)*3 => 9;
import re

def find_digit(text):
    numbers = re.compile('-?\d+')
    list_digit = list(map(int, numbers.findall(text)))
    return list_digit


def find_operations(text):
    pattern = '\D+'
    list_operations = re.findall(pattern, text)
    return list_operations


def calculator(list_digit, list_oper):
    for n in range(len(list_digit)):
        for i in range(len(list_oper)):
            if list_oper[i] == '*':
                list_digit[i] *= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break

        for i in range(len(list_oper)):
            if list_oper[i] == '/':
                list_digit[i] /= list_digit[i + 1]
                del list_digit[i + 1]
                del list_oper[i]
                break
    return list_digit


def result_operations(digits, operations):
    if len(digits) == len(operations):
        if operations[0] == '-':
            del operations[0]
    return operations


expression = input("Введите арифметического выражения: ")
expression = expression.replace(' ', '')

digits = find_digit(expression)
operations = find_operations(expression)
operations = result_operations(digits, operations)
result = sum(calculator(digits, operations))

print(f'{expression} = {result}')
