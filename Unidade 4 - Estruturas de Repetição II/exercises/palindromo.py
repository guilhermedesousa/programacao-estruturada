text = input("Insira algum texto: ")

isPalindromo = True

for i in range(len(text) // 2):
    if (text[i] != text[len(text) - 1 - i]):
        isPalindromo = False

if (isPalindromo):
    print('O texto ' + text + ' é palíndromo')
else:
    print('O texto ' + text + ' não é palíndromo')
