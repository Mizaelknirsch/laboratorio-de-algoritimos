maior_idade = 0
mulheres_verde_louro = 0

olhos_azuis = 0
olhos_verdes = 0
olhos_castanhos = 0

cabelos_loiros = 0
cabelos_castanhos = 0
cabelos_pretos = 0

sexo_m = 0
sexo_f = 0


for p in pessoas:
    sexo, olho, cabelo, idade = p

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and 18 <= idade <= 35 and olho == "V" and cabelo == "L":
        mulheres_verde_louro += 1

    if olho == "A":
        olhos_azuis += 1
    elif olho == "V":
        olhos_verdes += 1
    elif olho == "C":
        olhos_castanhos += 1

    if cabelo == "L":
        cabelos_loiros += 1
    elif cabelo == "C":
        cabelos_castanhos += 1
    elif cabelo == "P":
        cabelos_pretos += 1

    if sexo == "M":
        sexo_m += 1
    elif sexo == "F":
        sexo_f += 1


print("\n===== RESULTADOS =====")
print(f"Maior idade: {maior_idade}")
print(f"Mulheres (18-35 anos) com olhos verdes e cabelos louros: {mulheres_verde_louro}")

print("\nPorcentagem cor dos olhos:")
print(f"Azuis: {olhos_azuis/15*100:.2f}%")
print(f"Verdes: {olhos_verdes/15*100:.2f}%")
print(f"Castanhos: {olhos_castanhos/15*100:.2f}%")

print("\nPorcentagem cor dos cabelos:")
print(f"Loiros: {cabelos_loiros/15*100:.2f}%")
print(f"Castanhos: {cabelos_castanhos/15*100:.2f}%")
print(f"Pretos: {cabelos_pretos/15*100:.2f}%")

print("\nPorcentagem sexo:")
print(f"Masculino: {sexo_m/15*100:.2f}%")
print(f"Feminino: {sexo_f/15*100:.2f}%")
