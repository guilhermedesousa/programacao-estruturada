valor = int(input())
anterior = valor

for i in range(10):
    if i == 0:
        print('N[0] =', valor)
    else:
        print('N[' + str(i) + '] =', anterior * 2)
        anterior = anterior * 2
