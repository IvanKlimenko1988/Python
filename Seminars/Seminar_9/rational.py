import re

def find_digit(text):
    numbers = re.compile('-?\d+')
    list_digit = list(map(int, numbers.findall(text)))
    return list_digit


def find_operations(text):
    pattern = '\D+'
    list_operations = re.findall(pattern, text)
    return list_operations


def find_operations_priority(text):
    pattern = '.'
    list_operations = re.findall(pattern, text)
    return list_operations

def final_expression(text, text_1):
    new_str = ''
    index_start = text.index('(')
    index_end = text.index(')')
    for i in range(len(text)):
        if i < index_start or i > index_end:
            new_str+= text[i]
    result_srt = ''
    if new_str[0] == '*' or new_str[0] == '/' or new_str[0] == '-' or new_str[0] == '+':
        result_srt += str(text_1) + new_str
    elif new_str[-1] == '*' or new_str[-1] == '/' or new_str[-1] == '-' or new_str[-1] == '+':
        result_srt += new_str + str(text_1)
    return result_srt

def priority_decision(text):
    index_start = text.index('(')
    index_end = text.index(')')
    expression_priority = text[index_start+1:index_end]
    return expression_priority

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

def imput_text(text):
    expression = text
    expression = expression.replace(' ', '')
    if '(' and ')' in expression:
        expression_priority =  priority_decision(expression)
        digits_prior = find_digit(expression_priority)
        oper_prior = find_operations(expression_priority)
        oper_prior = result_operations(digits_prior, oper_prior)
        result_priority = sum(calculator(digits_prior, oper_prior)) # Резутьтат из скобок

        final_string = final_expression(expression, result_priority)
        final_digit = find_digit(final_string)
        final_oper = find_operations(final_string)
        final_oper = result_operations(final_digit,final_oper)
        result = sum(calculator(final_digit,final_oper))
        return result
    else:
        digits = find_digit(expression)
        operations = find_operations(expression)
        operations = result_operations(digits, operations)
        result = sum(calculator(digits, operations))
        return result