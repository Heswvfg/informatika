def fibo(x):
    if x in (1,2):
        return 1
    return fibo(x - 1) + fibo(x - 2)
x = int(input())
print(fibo(x))