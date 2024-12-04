print("page 10")
def convert(n, A):
    decimal = 0
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i, digit in enumerate(reversed(A)):
        decimal = decimal * n + digits.index(digit)
    return decimal
n = int(input("введите основание системы счисления (от 2 до 36): "))
A = input("введите число A: ")
decimal_A = convert(n, A)
print(f"число {A} в системе счисления с основанием {n} равно {decimal_A} в десятичной системе.")

print("page 12.1")

def contains_digit_3(number):
    tens = number // 10
    ones = number % 10
    return 3 in [tens, ones]
number = int(input("введите двузначное число: "))

if contains_digit_3(number):
    print(f"число {number} содержит цифру 3.")
else:
    print(f"число {number} не содержит цифры 3.")

print("page 12.2")

number1 = int(input("введите двузначное число: "))
tens1 = number1 // 10
ones1 = number1 % 10
if tens1>ones1:
    print(f"Наибольшая цифра: {tens1}")
else:
    print(f"Наибольшая цифра: {ones1}")

print("page 12.3")

import math
a = float(input("введите a (a ≠ 0): "))
b = float(input("введите b: "))
c = float(input("введите c: "))
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"два корня: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"один корень: x = {x}")
else:
    print("нет вещественных корней.")

print("page 15.1")

p=int(input("введите ваше число для нахождения наименьшего делителя:"))
h=[]
for y in range (1,10):
    if p%y==0:
        y=str(y)
        h.append(y)
print(f"наименьший целый делитель для числа {p} это: {h[1]}")

print("page 15.2")

N = int(input("введите число N (N < 1000): "))
if N >= 1000:
    print("число N должно быть меньше 1000.")
else:
    total_sum = N * (N + 1) // 2  
    print(f"сумма чисел от 1 до {N} равна {total_sum}.")

print("page 15.3")

num = int(input("введите натуральное число больше 1: "))
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(f"{num} {'является' if prime(num) else 'не является'} простым числом.")

print("page 15.4")

a4 = int(input("введите число a (a < 2^31): "))
n4 = int(input("введите основание n (2 ≤ n ≤ 9): "))
if 2 <= n4 <= 9:
    result1 = ""
    while a4 > 0:
        result1 = str(a4 % n4) + result1
        a4 //= n4
    print(f"ваше число в системе счисления с основанием {n4}: {result1}")
else:
    print("основание n должно быть от 2 до 9.")   