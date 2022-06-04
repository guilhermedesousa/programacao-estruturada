text = input("Insira algum texto: ")

for i in range(len(text) // 2):
    if (text[i] != text[len(text) - 1 - i]):
        print('O texto ' + text + ' não é palíndromo')
        break
else:
    print('O texto ' + text + ' é palíndromo')
