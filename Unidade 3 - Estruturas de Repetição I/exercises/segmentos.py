n = int(input("Informe um número n: "))
lst = []

for i in range(n):
    lst.append(int(input("Informe o " + str(i + 1) + "º número: ")))

anterior = lst[0]
seg = 1

for j in range(1, len(lst)):
    atual = lst[j]
    if (atual != anterior):
        seg += 1
        anterior = atual

print('Quantidade de segmentos de números iguais da sequência = ', seg)
