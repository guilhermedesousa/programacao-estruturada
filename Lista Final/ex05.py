valores = []

for i in range(10):
    valores.append(int(input()))

for j in range(10):
    if valores[j] <= 0:
        print('X[' + str(j) + '] =', 1)
    else:
        print('X[' + str(j) + '] =', valores[j])
