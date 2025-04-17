ontador = 0
soma_salario = 0
mulher10k = 0
menor_idade = 0
maior_idade = 0
while contador < 10:
    idade = int(input("digite a idade"))
    sexo = input("digite o sexo da pessoa:").upper()
    salario = float(input("digite o salario sa pessoa: "))

    if contador == 0:
        maior_idade = idade
        menor_idade = idade

    if maior_idade < idade:
        maior_idade = idade


    if menor_idade > idade:
        menor_idade = idade

    if sexo == "M" and salario <= 10000:


        contador =+ 1

    media_salarios = soma_salario / contador
    print("media dos salarios", maior_idade)
    print("maior idade ", maior_idade)
    print("menor idade ", menor_idade)
    print("quantidade de mulheres com salario ate 10k: ",mulher10k)
