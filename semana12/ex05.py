saldo = 0 


def mostrar_menu():
    print("\nMenu:")
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")

def sacar(valor):
    global saldo
    if valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Depósito de R${valor:.2f} realizado com sucesso.")


def mostrar_saldo():
    print(f"Saldo atual: R${saldo:.2f}")


while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor para saque: "))
        sacar(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor para depósito: "))
        depositar(valor)
    elif opcao == "3":
        mostrar_saldo()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
