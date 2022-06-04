def fib(n, call):
    call += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n - 1, call) + fib(n - 2, call)


n = int(input())
casos = []

for i in range(n):
    casos.append(int(input()))

for j in casos:
    cont = 0
    calls = 0
    result = fib(j, calls)
    print(result)
