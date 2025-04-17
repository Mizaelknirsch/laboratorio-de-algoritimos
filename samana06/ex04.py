soma_idades = 0
maiores_de_idade = 0
entre_10_e_30 = 0
contador = 1
while contador <= 7:
    idade = int(input(f"Digite a idade da {contador}ª pessoa: "))
    soma_idades += idade
    if idade >= 18:
        maiores_de_idade += 1
    elif 10 <= idade <= 30:
        entre_10_e_30 += 1
    contador += 1
media = soma_idades / 7
porcentagem_10_30 = (entre_10_e_30 / 7) * 100
print(f"\nMédia das idades:",media)
print(f"Quantidade de pessoas maiores de idade: {maiores_de_idade}")
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos: {porcentagem_10_30}%")
