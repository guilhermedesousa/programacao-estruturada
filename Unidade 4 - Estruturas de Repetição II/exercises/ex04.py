rodada = 1
vitBob = 0
vitAlice = 0

while (rodada <= 7 and vitBob < 4 and vitAlice < 4):
    jogBob = int(input('Qual sua jogada, Bob? '))
    jogAlice = int(input('Qual sua jogada, Alice? '))
    sumJog = jogBob + jogAlice

    if (sumJog % 2 == 0):
        vitAlice += 1
    else:
        vitBob += 1

    rodada += 1

if (vitBob == 4):
    print('Parabéns, Bob!')
else:
    print('Parabéns, Alice!')
