n = int(input("Qual o valor de n? "))
cont = 1

while cont <= n:
    estrelas = ''
    for i in range(cont):
        estrelas += '*'
    print(estrelas)

    cont += 1
