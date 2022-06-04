phrase = input('Qual a frase? ')
phraseWithoutSpace = phrase.replace(" ", "")

ehPalindromo = True
phraseSize = len(phraseWithoutSpace)
cont = 0

while (cont < (phraseSize // 2)):
    if phraseWithoutSpace[cont] != phraseWithoutSpace[phraseSize - 1 - cont]:
        print('A frase não é um palíndromo!')
        break
    else:
        cont += 1
else:
    print('A frase é um palíndromo!')
