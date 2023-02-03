# 2. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
staert_list = [1, 2, 3, 4, 5]
num = 6
k = num % len(staert_list)
# -> [3, 4, 5, 1, 2]
list_result = staert_list.copy()
for i in range(len(staert_list)):
    if (i + k) < len(staert_list):
        list_result[i + k] = staert_list[i]
    else:
        list_result[i + k - len(list_result)] = staert_list[i]
print(list_result)



for i in range(len(staert_list)):
    temp = staert_list[i]
    staert_list[i] = staert_list[i + k]
    staert_list[i + k] = temp
print(staert_list)



