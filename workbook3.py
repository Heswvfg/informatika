print("page 12.1")
import math

x = float(input('Введите x '))
y = float(input('Введите y '))
f = math.log(math.sin(x + y))
print('f = ', f)

print("page 12.2")

x = float(input('Введите x '))
y = float(input('Введите y '))

if math.sin(x+y)<=-0.5:
    f=math.atan((pow(x-y)**1/3) * (x*math.e**y))
elif -0.5<math.sin(x+y)<0.5:
    f=3*math.log(pow(x*y),[3])
elif math.sin(x+y)>=0.5:
    f=x**3+y**1.5
print("f = ", f)

print("page 12.3")

def f(x):
    return math.cos(3 * math.exp(x)) + math.sin(abs(x))

a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
hx = float(input("Введите шаг hx: "))

x = a
while x <= b:
    print(f"f({x:.2f}) = {f(x):.2f}")
    x += hx

print("page 13")

def f(x, y):
    if x + y <= 2:
        return (math.sin(x * math.exp(0.1 * y)))**(1/3)
    elif x + y > 2:
        return math.pow(math.log2(x + y), 2)
ax = 1
bx = 2.5    
ay = 1    
by = 4
x = ax
while x <= bx:
    y = ay
    while y <= by:
        print(f"f({x:.2f}, {y:.2f}) = {f(x, y):.2f}")
        y += 1
        x += 0.5

