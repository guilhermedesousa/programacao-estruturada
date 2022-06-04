def fib(n):
    f2 = 0
    f1 = 1
    if n == 0:
        return f2
    if n == 1:
        return f1
    else:
        for x in range(0, n - 1):
            f0 = f1 + f2
            f2 = f1
            f1 = f0
        return f0


n = int(input())
casosDeTeste = []

for i in range(n):
    casosDeTeste.append(int(input()))

for j in casosDeTeste:
    print('Fib(' + str(j) + ') =', fib(j))
