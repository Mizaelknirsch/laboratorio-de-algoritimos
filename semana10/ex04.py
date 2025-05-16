vetor_A = []


while len(vetor_A) < 10:
    valor = int(input(f"Digite o valor {len(vetor_A)+1}: "))
    if valor in vetor_A:
        print("Valor já foi digitado! Digite um valor diferente.")
    else:
        vetor_A.append(valor)

print(f"Vetor A: {vetor_A}")


vetor_B = vetor_A[::-1]

print(f"Vetor B (ordem inversa): {vetor_B}")
