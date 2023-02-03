# 3. Напишите программу для печати всех уникальных значений в словаре.
d = {1: 'Vlad', 2: 'Vlad', 3: 'Oleg', 4:'Oleg', 5:'Vlad'}

# len_dict = len(d)

# list = []
# i = 1

# while i <= len_dict:
#     list.append(d.get(i))
#     i += 1

list_1 = d.values()

print(len(set(list_1)))


