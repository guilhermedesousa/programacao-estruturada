coordenadas = ''

while coordenadas != '0,0':
    coordenadas = input("Entre com as coordenadas na forma x,y: ")
    arrayCoord = coordenadas.split(",")
    x = int(arrayCoord[0])
    y = int(arrayCoord[1])

    if (x != 0 and y != 0):
        if (x == 0):
            msg = 'Você está sobre o eixo y.'
        elif (y == 0):
            msg = 'Você está sobre o eixo x.'
        elif (x > 0):
            if (y > 0):
                msg = 'Você está no 1º quadrante.'
            else:
                msg = 'Você está no 4º quadrante.'
        elif (x < 0):
            if (y > 0):
                msg = 'Você está no 2º quadrante.'
            else:
                msg = 'Você está no 3º quadrante.'

        print(msg)
