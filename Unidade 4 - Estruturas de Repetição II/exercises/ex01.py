n = int(input("Digite o valor do número: "))
qtdPar = 0

while n != 0:
    if (n % 2 == 0):
        print('é par')
        qtdPar += 1
    else:
        print('é ímpar')

    n = int(input("Digite o valor do número: "))

print('foram lidos ' + str(qtdPar) + ' números pares.')
