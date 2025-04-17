contagem = 0
saldo = float(input("qual seu saldo: "))
while contagem != 4:
    print("1 sacar")
    print("2 depositar")
    print("3 saldo")
    print("4 sair")
    contagem = float(input("digite uma opção: "))
    if contagem == 1:
        saldo = saldo - float(input("quando você deseja sacar: "))
    elif contagem == 2:
        saldo = saldo + float(input("digite o valor que você deseja depositar: "))
    elif contagem == 3:
        print("o seu saldo atual é ",saldo)
