def soma_naturais(n):
    if n < 0:
        return 0  
    return n * (n + 1) // 2

while True:
    entrada = input("Digite um número natural para somar até ele (ou 'sair' para encerrar): ")

    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break

    try:
        numero = int(entrada)
        if numero < 0:
            print("Por favor, digite um número natural (0 ou maior).")
        else:
            resultado = soma_naturais(numero)
            print(f"A soma dos números naturais até {numero} é: {resultado}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro ou 'sair'.")
