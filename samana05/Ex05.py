um1 = float(input("Digite o primeiro numero: "))
print("+ - * /")
opcao = str(input("Digite qual opçao quer usar: "))
num2 = float(input("Digite o sugundo numero: "))
divi = num1 / num2


if opcao == "+":
    soma = num1 + num2
    print("resposta: ", soma)


elif opcao == "-":
    menos = num1 - num2
    print("resposta: ", menos)

elif opcao == "*":
    vezes = num1 * num2
    print("resposta: ", vezes)


if num2 == 0 and opcao == "/":
    print("erro tente novamente!!")

else: 
    divi = num1 / num2
    print("resposta: ", divi)
