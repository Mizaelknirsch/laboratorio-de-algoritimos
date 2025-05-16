A = []


for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor (distinto): "))
    while valor in A:
        print("Valor repetido! Digite um valor distinto.")
        valor = int(input(f"Digite o {i+1}º valor novamente: "))
    A.append(valor)


B = A[::-1]


print("\nVetor A:", A)
print("Vetor B (invertido):", B)
