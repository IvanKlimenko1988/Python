# Задача 1
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def find_degree_of_num(a, b):
    if b == 1:
        return a
    return a * find_degree_of_num(a, b - 1)


a = int(input("--> А: "))
b = int(input("--> B: "))
print(f"A = {a}; B = {b} -> {find_degree_of_num(a, b)}")
