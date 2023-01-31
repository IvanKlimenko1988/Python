n = int(input('n: '))
f_1 = 1
f_2 = 1
num_index = 2

while f_2 < n:
    num_index += 1
    f_1, f_2 = f_2, f_1 + f_2
    
if f_2 == n:
    print(num_index)
else:
    print(-1)
    
print(num_index if f_2 == n else -1)