num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if num1 > num2:
    print("o maior é", num1 )
    print("depois vem: ", num2)

elif num2 > num1:
    print("o maior é", num2)
    print("depois vem: ", num1)

elif num1 == num2:
    print("ERRO tente novamente!!!")
