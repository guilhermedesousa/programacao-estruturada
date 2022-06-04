palavra = input("Digite a palavra: ")

tamanho = len(palavra)

for i in range(0, tamanho):
    if (palavra[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']):
        print("A palavra contem a vogal ", palavra[i])
        break
else:
    print("A palavra não contem nenhuma vogal")
