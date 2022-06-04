vetor = []

for i in range(100):
    vetor.append(float(input()))

for j in range(100):
    if vetor[j] <= 10:
        print('A[' + str(j) + '] =', vetor[j])
