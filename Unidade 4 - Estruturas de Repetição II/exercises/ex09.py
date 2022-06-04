nota = 0
listaNotas = []
sumNotas = 0
qtdNotas = 0

while (0 <= nota <= 10):
    nota = float(input("Informe uma nota: "))
    if (nota < 0 or nota > 10):
        break
    else:
        sumNotas += nota
        qtdNotas += 1
        listaNotas.append(nota)

media = sumNotas / qtdNotas
acimaDaMedia = 0

for i in listaNotas:
    if i >= media:
        acimaDaMedia += 1

print('A média é', media, 'e há', acimaDaMedia, 'notas acima dela.')
