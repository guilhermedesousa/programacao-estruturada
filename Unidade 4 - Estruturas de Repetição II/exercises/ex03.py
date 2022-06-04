rodar = True
tentativas = 1

while (rodar and tentativas <= 3):
    senha = int(input("Digite a sua senha numérica: "))
    if senha == 1234:
        print("SENHA CORRETA")
        rodar = False
    else:
        tentativas += 1
        print("SENHA INCORRETA")

if (tentativas > 3):
    print('Você ultrapassou o limite de tentativas :(')
