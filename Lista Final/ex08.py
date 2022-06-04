vetor = []

for i in range(20):
    vetor.append(int(input()))

for j in range(20):
    if (j < 10):
        elemento1 = vetor[j]
        elemento2 = vetor[len(vetor) - 1 - j]
        vetor[j] = elemento2
        vetor[len(vetor) - 1 - j] = elemento1

    print('N[' + str(j) + '] =', vetor[j])
