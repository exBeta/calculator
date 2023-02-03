def calc(x, y):
    summa = x + y
    difference = x - y
    multiplication = x * y
    try:
        division = x / y
    except ZeroDivisionError:
        division = "Деление на ноль не возможно"
    return summa, difference, multiplication, division


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
except ValueError:
    print("Вы указали не целочисленное значение")

summa, difference, multiplication, division = calc(a,b)
print(f"{a}+{b}={summa}")
print(f"{a}-{b}={difference}")
print(f"{a}*{b}={multiplication}")
if b != 0:
    print(f"{a}/{b}={division}")
else:
    print(division)