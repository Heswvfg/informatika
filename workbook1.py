print('Часть 1')

print('Громилин Андрей ЭФБО-15-24')

a=int(input('Введите число а'))
b=int(input('Введите число б'))
print(a+b)

x=float(input("введите значение для x"))
y=x**5-2*x**3+1
print('значение y: ', y)

print('Часть 2')

strange=[[],1]
print('тип переменной strange: ', type(strange))

for x in range(2):
    for y in range(2):
        if (x or y) and (not(x) or y) and not(x and y)==1:
            print('x y')
            print(x,y)

list=[1234]
list.sort(reverse=True)
print(list)

print('Часть 3')
import math
n = int(input("введите количество состояний: "))
h = math.log2(n)
print(f"количество состояний: {n}")
print(f"формула Хартли: {h:.2f}")

p1 = float(input("введите вероятность 1 состояния: "))
p2 = float(input("введите вероятность 2 состояния: "))
h = -(p1 * math.log2(p1) + p2 * math.log2(p2))
print(f"энтропия (Шен): {h:.2f}")

x3 = float(input("введите значение x: "))
p1= math.tan(math.cos(x3) * math.sin(2 * x3) / x * math.exp(x3))
logg = math.log(x3, 7)
result = p1 **  logg
print(f"результат: {result:.2f}")

def add_parity_bit(byte):
    num_ones = sum(byte)
    parity_bit = 1 if num_ones % 2 == 1 else 0
    byte.append(parity_bit)
    return byte
byte = [1, 0, 1, 1, 0, 0, 1, 0]
byte_with_parity = add_parity_bit(byte)
print("исходный байт:", byte, "байт с битом четности:", byte_with_parity)