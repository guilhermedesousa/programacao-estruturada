numero = int(input())

for i in range(numero):
    numeroDePessoas = int(input())
    idiomas = []
    for j in range(numeroDePessoas):
        idiomas.append(input())

    escolha = 'ingles'
    exemplo = idiomas[0]

    for k in idiomas:
        if k != exemplo:
            break
    else:
        escolha = idiomas[0]

    print(escolha)
