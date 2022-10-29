# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import re

def rle_compression(text):
    count = 1
    rle_str = ''
    i = 0
    while i < len(text):
        for j in range(len(text) - 1):
            if i >= len(text):
                break
            else:
                if text[i] == text[j + 1]:
                    count += 1
                    i += 1
                else:
                    rle_str += str(count) + text[i]
                    count = 1
                    i += 1
    return rle_str

def rle_recovery(text):
    res_str = ''
    num_filtr = re.compile('-?\d+')
    list_num = list(map(int, num_filtr.findall(code)))
    j = 0
    for i in range(len(code)):
        if not code[i].isdigit():
            res_str += str(code[i]) * list_num[j]
            j += 1
    return res_str

inmort_string = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'



code = rle_compression(inmort_string)
print(code)

de_code = rle_recovery(code)
print(de_code)




