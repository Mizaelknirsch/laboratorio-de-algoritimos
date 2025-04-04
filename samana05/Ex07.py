nome = str(input("Digite sei nome:"))
salario = float(input("Digite seu salario: "))
tempo = float(input("Digite quanto tempo trabalha na empresa "))
if tempo >= 5 and salario <= 2000:
    resto1 =  salario * 1.10
    print("seu novo salario com 10% a mais: ", resto1)

else:
    tempo < 5 and salario > 2000
    resto2 = salario * 1.05
    print("seu novo salario com 5% a mais: ", resto2)
