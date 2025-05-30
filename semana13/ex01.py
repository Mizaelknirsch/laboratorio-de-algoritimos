def eh_primo(n):

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    entrada = input("Digite um número inteiro para verificar se é primo (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    try:
        numero = int(entrada)
        if eh_primo(numero):
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")
