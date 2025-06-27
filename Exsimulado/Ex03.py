def inserir_faturamento():
    faturamento = []
    for i in range(4):
        while True:
            try:
                valor = float(input(f"Digite o faturamento da semana {i + 1} (em R$): "))
                faturamento.append(valor)
                break
            except ValueError:
                print("Por favor, digite um número válido.")
    return faturamento

def exibir_faturamento(faturamento):
    print("\nFaturamento por semana:")
    for i, valor in enumerate(faturamento):
        print(f"Semana {i + 1}: R$ {valor:.2f}")

def calcular_estatisticas(faturamento):
    media = sum(faturamento) / len(faturamento)
    maior_valor = max(faturamento)
    semana_maior = faturamento.index(maior_valor) + 1

    print(f"\nMédia mensal de faturamento: R$ {media:.2f}")
    print(f"Semana com maior faturamento: Semana {semana_maior} (R$ {maior_valor:.2f})")

    print("\nVariação de uma semana para a seguinte:")
    for i in range(3):
        atual = faturamento[i]
        proxima = faturamento[i + 1]
        variacao = ((proxima - atual) / atual) * 100 if atual != 0 else 0
        print(f"Semana {i + 1} -> Semana {i + 2}: {variacao:.2f}% {'a mais' if variacao > 0 else 'a menos' if variacao < 0 else 'sem variação'}")

def alterar_faturamento(faturamento):
    while True:
        try:
            semana = int(input("Digite o número da semana que deseja alterar (1 a 4): "))
            if 1 <= semana <= 4:
                novo_valor = float(input("Digite o novo valor de faturamento (em R$): "))
                faturamento[semana - 1] = novo_valor
                print(f"Faturamento da semana {semana} alterado com sucesso.")
                break
            else:
                print("Número de semana inválido. Digite entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def main():
    faturamento = [0.0, 0.0, 0.0, 0.0]
    while True:
        print("\n=== MENU ===")
        print("1 - Inserir faturamento das 4 semanas")
        print("2 - Exibir faturamento por semana")
        print("3 - Mostrar estatísticas")
        print("4 - Alterar valor de uma semana")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            faturamento = inserir_faturamento()
        elif opcao == '2':
            exibir_faturamento(faturamento)
        elif opcao == '3':
            calcular_estatisticas(faturamento)
        elif opcao == '4':
            alterar_faturamento(faturamento)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
