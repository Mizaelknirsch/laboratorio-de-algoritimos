import random
guardioes = []
invasores = []
contador = 0
for i in range(5):
    i = random.randint(0, 100)
    invasores.append(i)
while contador < 5:
    try:
        i = int(input(f"digite o ataque do {contador+1}º guardião: "))
        guardioes.append(i)
        contador += 1
    except:
        print("digite um número inteiro")
for i in range(5):
    if invasores[i] > guardioes[i]:
        print(f"a defesa do {i+1}º invasor é {invasores[i]} e o ataque do {i+1}º guardião é {guardioes[i]}, o guardião perdeu a batalha")
    elif invasores[i] == guardioes[i]:
        print(f"a defesa do {i+1}º invasor é {invasores[i]} e o ataque do {i+1}º guardião é {guardioes[i]}, invasor resistiu")
    else:
        print(f"a defesa do {i+1}º invasor é {invasores[i]} e o ataque do {i+1}º guardião é {guardioes[i]}, guardião ganhou a batalha")
