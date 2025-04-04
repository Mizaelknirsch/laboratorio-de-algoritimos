nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
frequencia = int(input("digite sua frequencia em %:"))
cal1 = (nota1 + nota2) / 2 

if cal1 >= 7 and frequencia >= 75:
    print("aprovado!!", cal1)

elif cal1 >= 4 and cal1 < 7 and frequencia > 75:
    print("Exame: ",cal1)

elif cal1 < 4 and frequencia < 75:
    print("REPROVADO", cal1)
