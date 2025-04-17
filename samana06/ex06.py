contador_maiores_18 = 0
contador = 1
while contador <= 10:
    idade = int(input(f"Digite a idade da {contador}ª pessoa: "))
    if idade >= 18:
        contador_maiores_18 += 1
    contador += 1
print("Quantidade de pessoas com 18 anos ou mais:", contador_maiores_18)
