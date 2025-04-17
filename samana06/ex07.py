contador_entre_30_e_90 = 0
contador = 1
while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))
    if numero >= 30 and numero <= 90:
        contador_entre_30_e_90 += 1
    contador += 1
print(f"Quantidade de números entre 30 e 90: {contador_entre_30_e_90}")
