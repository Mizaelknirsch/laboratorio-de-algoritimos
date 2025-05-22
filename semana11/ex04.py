numeros = []
contador = 0
contador2 = -1
pmaior = 0
pmenor = 0
while contador < 5:
    try:
        i = int(input("digite um número: "))
        numeros.append(i)
        contador += 1
        maior = numeros[0]
        menor = numeros[0]
    except:
        print("digite um número inteiro")
for i in numeros:
    if maior < i:
        maior = i
        contador2 += 1
        pmaior = contador2
    elif menor > i:
        menor = i
        contador2 += 1
        pmenor = contador2
    else:
        contador2 += 1
print(f"o maior número é {maior}, que está na posição {pmaior}")
print(f"o menor número é {menor}, que está na posição {pmenor}")
