# Задача 4: Требуется определить, можно ли от шоколадки размером
# n × m долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите n: "))
m = int(input("Введите m: "))
k = int(input("Введите k: "))
answer = "no"
if ((n * m - k) % 2 == 0):
    answer = "yes"
print(f"{n} {m} {k} -> {answer}")
