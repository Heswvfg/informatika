print("14.1")

k = int(input("Введите число k: "))
n = int(input("Введите число n: "))
result = (1 << k) + (1 << n)
print(f"Результат: {result}")

print("page 14.2")

n = int(input("Введите число n > 0: "))
j=[]
for t in range(100):
    t=2**t
    if n==t:
        j.append("YES")
    else:
        j.append("NO")
if "YES" in j:
    print("YES")
else:
    print("NO")

print("page 14.3")

a = int(input("Введите число a: "))
k = int(input("Введите позицию бита k: "))
result = a | (1 << k)
print(f"Результат: {result}")

print("page 14.4")

n = int(input("Введите число n: "))
k = int(input("Введите количество бит k: "))
result = n >> k << k
print(f"Результат: {result}")