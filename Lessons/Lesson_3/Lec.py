# Анонимные, lambda функции:

def sum(x):
    return x+10


def mult(x):
    return x**2


print(sum(mult(2)))  # 2*2 + 10= 14


def sum1(x):
    return x+22


def mult2(x):
    return x**3


print(sum1(mult2(2)))  # 2*2*2 + 22= 30


def sum3(x):
    return x+242


def mult4(x):
    return x**5


print(sum3(mult4(2)))  # 2*2*2*2*2 + 242= 274


# В переменную можно записывать функию!


