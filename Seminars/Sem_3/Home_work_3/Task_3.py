# 3. В настольной игре Скрабл каждая буква имеет определенную ценность
# В случае с английским алфавитом очки распледеляюся так
# A E I O U L N S T R  - 1 очко. D G - 2 очка. B C M P - 3 очка
# F H V W Y - 4 очка. K - 5 очков. J X - 8 очков. Q Z - 10 очков
# А русские буквы оцениваются так А В Е И Н О Р С Т - 1 очко
# Д К Л М П У - 2 очка. Б Г Ё Ь Я - 3 очка. Й Ы - 4 очка. Ж З Х Ц Ч - 5 очков. Ш Э Ю
# - 8 очков. Ф Щ Ъ - 10 очков. Напишите программу которая вычисляет стоимость введеного
# пользователем слова. Будем считать что на вход подаётся одно слово которое содержит
# либо только русские либо латинские буквы

# ноутбук - 12


points_eng = {1: ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R"],
              2: ["D", "G"],
              3: ["B", "C", "M", "P"],
              4: ["F", "H", "V", "W", "Y"],
              5: ["K"],
              8: ["J", "X"],
              10: ["Q", "Z"]}

points_rus = {1: ["А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"],
              2: ["Д", "К", "Л", "М", "П", "У"],
              3: ["Б", "Г", "Ё", "Ь", "Я"],
              4: ["Й", "Ы"],
              5: ["Ж", "З", "Х", "Ц", "Ч"],
              8: ["Ш", "Э", "Ю"],
              10: ["Ф", "Щ", "Ъ"]}

word = "notebook".upper()
list_char = []
for i in word:
    list_char.append(i)

print(list_char)

sum=0
for i in list_char:
    for k,v in points_rus.items():
        if i in v:
            sum+=k

    for k,v in points_eng.items():
        if i in v:
            sum+=k



# sum = 0
# for key, value in points_rus.items():
#     for i in list_char:
#         if i in value:
#             sum += key
#         else:
#             for key, value in points_eng.items():
#                 for i in list_char:
#                     if i in value:
#                         sum += key



# if list_char in points_rus.values():
#     for key, value in points_eng.items():
#         for i in list_char:
#             if i in value:
#                 sum += key


    # print(f"{key} {value}")

print(sum)