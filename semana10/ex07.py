for i in range(10):
    numero = int(input(f"Digite o {i+1}º valor: "))
    while numero in valores:
        print("Valor repetido! Digite um valor distinto.")
        numero = int(input(f"Digite o {i+1}º valor novamente: "))
    valores.append(numero)

# Mostrar pares e suas posições
print("\nNúmeros pares e suas posições:")
for i in range(10):
    if valores[i] % 2 == 0:
        print(f"Valor {valores[i]} na posição {i}")
