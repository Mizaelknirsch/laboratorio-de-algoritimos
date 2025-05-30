



numeros = []

print("Por favor, digite 10 números inteiros:")

while len(numeros) < 10:
    try:
        n = int(input(f"Digite o número {len(numeros) + 1}: "))
        numeros.append(n)
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

lista_sem_repetidos = []
for num in numeros:
    if num not in lista_sem_repetidos:
        lista_sem_repetidos.append(num)

print("\nNúmeros digitados:", numeros)
print("Números sem repetições:", lista_sem_repetidos)
