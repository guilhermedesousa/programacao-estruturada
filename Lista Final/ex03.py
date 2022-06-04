entrada = input()

while entrada != '0 0':
    caso = entrada.split(' ')
    digito = caso[0]
    numero = caso[1]

    numeroNoContrato = ''

    for i in numero:
        if i != digito:
            numeroNoContrato += i

    if (numeroNoContrato == ''):
        numeroNoContrato = 0
    else:
        numeroNoContrato = int(numeroNoContrato)

    print(numeroNoContrato)

    entrada = input()
