qtdChances = 1

while (True):
    if qtdChances > 3:
        break
    else:
        senha = int(input("Digite a sua senha numérica: "))
        if senha == 1234:
            print("SENHA CORRETA")
            break
        else:
            qtdChances += 1
            print("SENHA INCORRETA")

if (qtdChances > 3):
    print("VOCÊ ERROU AS TRÊS TENTATIVAS")
