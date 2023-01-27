# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Введите трёхзначное число: "))
hund = num // 100
dozen = (num // 10) - (hund * 10)
unit = num - num // 10 * 10
resut = hund + dozen + unit
print(f"Сумма чисел числа {num} -> {resut} ({hund} + {dozen} + {unit})")