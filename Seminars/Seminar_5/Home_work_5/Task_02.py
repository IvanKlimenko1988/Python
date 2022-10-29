# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# numbers = int(print("Введите последовательность чисел: "))


# numbers = 10000100001111111110111110000000000000011111111
numbers = 1011
str_1 = str(numbers)
count = 1
num = []
cnt = []

# for i in range(len(str_1)-1):
#     if i <= len(str_1):
#         if str_1[i] == str_1[i + 1]:
#             count +=1
#             num.append(str_1[i])
            
#         else:
            
#             cnt.append(count)
#             num.append(str_1[i])
#             count = 1
          
            
# print(len(str_1))
# print(len(num))
# print(num)
# print(cnt)
       
numbers = 10000100001111111110111110000000000000011111111
str_1 = str(numbers)
cout = 1
for i in range(len(str_1)-1):
    if i <= len(str_1):
        if str_1[i] == str_1[i + 1]:
            cout += 1
            num.append(str_1[i])
        else:
            a = str_1[i]
            print(cout, str_1[i])
            cnt.append(count)
            num.append(str_1[i])
            cout = 1
print(cout, str_1[i])

            
print(len(str_1))
print(len(num))
print(num)
print(cnt)