#   1. За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

#**Input:**
n = 700
m = 750
t = (m + n - 1) // n
print(t)
#**Output:** 2

#   2. Орудовать кабинеты для них новыми партами. 
#За каждой партой может сидеть два учащихся. 
##Известно количество учащихся в каждом из трех классов. 
#Выведите наименьшее число парт, которое нужно приобрести для них.

#**Input:**
n = int(input("Введите n: "))#20
m = int(input("Введите m: "))#21 
k = int(input("Введите k: "))#22
print((n + 1) // 2 + (m + 1) // 2 + (k + 1)//2)
#**Output:** 32

#   3 Вагоны в электричке пронумерованы натуральными числами, 
# начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, 
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). 
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке. 
# Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.

# **Input:**
# 3
# 4
i = int(input('--> ' ))
j = int(input('--> ' ))
if (i == j):
    print("Vitya ne mozhet pochitat'")
else:
    print(i + j - 1, "vagonov")
# **Output:**
# 6

