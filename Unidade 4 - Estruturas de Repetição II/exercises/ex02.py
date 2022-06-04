opcao = 0

while opcao != 5:
    print("Menu")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Terminar o programa")

    opcao = int(input("Digite a opção desejada: "))

    validOptions = [1, 2, 3, 4, 5]

    if (opcao not in validOptions):
        print('Por favor, informe uma opção válida!')
    elif (opcao != 5):
        number1 = float(input('Qual o primeiro operando? '))
        number2 = float(input('Qual o primeiro operando? '))

        if (opcao == 1):
            print(str(number1) + ' + ' + str(number2) +
                  ' = ' + str(number1 + number2))
        elif (opcao == 2):
            print(str(number1) + ' - ' + str(number2) +
                  ' = ' + str(number1 - number2))
        elif (opcao == 3):
            print(str(number1) + ' x ' + str(number2) +
                  ' = ' + str(number1 * number2))
        elif (opcao == 4):
            print(str(number1) + ' / ' + str(number2) +
                  ' = ' + str(number1 / number2))
