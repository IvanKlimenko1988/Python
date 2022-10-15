#  Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

start_number = input('Введите вещественное или целое число: ')

def sum_digits(number):
    try:
        substring = '.'
        if substring in number:     # Поиск точки в строке
                length = len(number)
                num = float(number)
                current = 0
                while current < length - 1:
                    num *= 10
                    current += 1
                current = num
                sum = 0
                while current > 0:
                    sum += current % 10
                    current //= 10
                print(round(sum))
        else:
            num = int(number)
            current = num
            sum = 0
            while current > 0:
                sum += current % 10
                current //= 10
            print(sum)
    except:
        print("Введите правильное число")

sum_digits(start_number)
