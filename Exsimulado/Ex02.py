def ler_tamanho_array():
    while True:
        try:
            tamanho = int(input("Digite o tamanho do array: "))
            if tamanho > 0:
                return tamanho
            else:
                print("O número deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def preencher_array(tamanho):
    numeros = []
    for i in range(tamanho):
        while True:
            try:
                num = int(input(f"Digite o {i + 1}º número: "))
                numeros.append(num)
                break
            except ValueError:
                print("Digite um número inteiro.")
    return numeros

def mostrar_array(array):
    while True:
        print("\nMenu de Exibição:")
        print("1 - Mostrar todos os valores (um por linha)")
        print("2 - Mostrar valores ímpares e múltiplos de 3")
        print("3 - Mostrar valores nas posições ímpares e múltiplos de 5")
        print("4 - Mostrar os valores invertidos")
        print("5 - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nTodos os valores:")
            for num in array:
                print(num)

        elif opcao == '2':
            print("\nValores ímpares e múltiplos de 3:")
            for num in array:
                if num % 2 != 0 and num % 3 == 0:
                    print(num)

        elif opcao == '3':
            print("\nValores nas posições ímpares e múltiplos de 5:")
            for i in range(1, len(array), 2):  # posições ímpares (começando em 0)
                if array[i] % 5 == 0:
                    print(array[i])

        elif opcao == '4':
            print("\nValores invertidos:")
            for num in reversed(array):
                print(num)

        elif opcao == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")

def main():
    array = []
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Criar novo array")
        print("2 - Mostrar array")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tamanho = ler_tamanho_array()
            array = preencher_array(tamanho)

        elif escolha == '2':
            if len(array) == 0:
                print("O array ainda está vazio. Crie um primeiro!")
            else:
                mostrar_array(array)

        elif escolha == '3':
            print("Programa finalizado.")
            break

        else:
            print("Opção inválida. Digite 1, 2 ou 3.")

main()
