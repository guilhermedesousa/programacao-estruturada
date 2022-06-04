anosInput = input("Informe os anos que quer analisar separados por ',': ")
anos = anosInput.split(",")
ano = int(anos[0])
cont = 0

while (ano > 0 and cont < len(anos)):
    ano = int(anos[cont])

    if (ano % 4 == 0):
        if (ano % 100 == 0 and ano % 400 != 0):
            print('O ano', ano, 'não é bissexto')
        else:
            print('O ano', ano, 'é bissexto')
    else:
        print('O ano', ano, 'não é bissexto')

    cont += 1
