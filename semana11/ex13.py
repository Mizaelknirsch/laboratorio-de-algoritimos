itens = []
while True:
    print("\nMenu:")
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar item")
    print("4 - Retirar todos os itens")
    print("5 - Contar itens maiores que um valor X")
    print("6 - Verificar se um número está presente")
    print("7 - Encontrar o maior e o menor item")
    print("8 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Digite um número válido.")

    if opcao == 1:
        try:
            n = int(input("Digite um número PAR para inserir: "))
            if n % 2 == 0:
                itens.append(n)
                print(f"{n} foi adicionado à lista.")
            else:
                print("Erro: Apenas números pares são permitidos!")
        except:
            print("Erro: Digite um número inteiro válido.")

    elif opcao == 2:
        if itens:
            print("Itens da lista:", itens)
        else:
            print("A lista está vazia.")

    elif opcao == 3:
        try:
            n = int(input("Digite o número a ser removido: "))
            if n in itens:
                itens.remove(n)
                print(f"{n} foi removido da lista.")
            else:
                print("Número não encontrado na lista.")
        except:
            print("Erro: Digite um número inteiro válido.")

    elif opcao == 4:
        itens = []
        print("Todos os itens foram removidos.")

    elif opcao == 5:
        try:
            x = int(input("Digite o valor X: "))
            contador = 0
            for item in itens:
                if item > x:
                    contador += 1
            print(f"Quantidade de itens maiores que {x}: {contador}")
        except:
            print("Erro: Digite um número inteiro válido.")

    elif opcao == 6:
        try:
            n = int(input("Digite o número que deseja procurar: "))
            if n in itens:
                print(f"{n} está presente na lista.")
            else:
                print(f"{n} não está presente na lista.")
        except:
            print("Erro: Digite um número inteiro válido.")

    elif opcao == 7:
        if itens:
            maior = max(itens)
            menor = min(itens)
            print(f"Maior item: {maior}")
            print(f"Menor item: {menor}")
        else:
            print("A lista está vazia.")

    elif opcao == 8:
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Escolha uma opção de 1 a 8.")
