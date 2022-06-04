n = int(input())
entradas = []
alfabeto = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K',
            'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']

for i in range(n):
    entradas.append(input())

for j in entradas:
    texto = list(j)
    tam = len(texto)

    # deloca a letra
    for k in range(tam):
        letra = texto[k]
        if (letra in alfabeto):
            letra = chr(ord(letra) + 3)
            texto[k] = letra

    # inverte o texto
    textoInvertido = []
    for l in range(tam):
        textoInvertido.append(texto[tam - 1 - l])

    # desloca a letra
    textoCriptografado = ''
    for m in range(tam):
        if (m < tam // 2):
            textoCriptografado += textoInvertido[m]
        else:
            textoCriptografado += chr(ord(textoInvertido[m]) - 1)

    print(textoCriptografado)
