n = int(input("Informe um número n: "))
numbersList = []

for i in range(n):
    numbersList.append(int(input("Digite o " + str(i + 1) + "º número: ")))

sumMax = numbersList[0]

for j in range(0, len(numbersList)):
    sumAtual = numbersList[j]
    if (sumAtual > sumMax):
        sumMax = sumAtual
    for k in range(j + 1, len(numbersList)):
        sumAtual = sumAtual + numbersList[k]
        if (sumAtual > sumMax):
            sumMax = sumAtual

print('O segmento de soma máxima vale:', sumMax)
