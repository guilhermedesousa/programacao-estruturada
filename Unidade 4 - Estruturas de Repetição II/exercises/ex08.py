m = int(input("Informe um número inteiro: "))

for i in range(2, m + 1):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)
