# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

n = int(input("Введите число N: "))

result = 2
step = 0
while result < n:
    result = 2
    result **= step
    step += 1
    if result > n:
        continue
    print(result)



