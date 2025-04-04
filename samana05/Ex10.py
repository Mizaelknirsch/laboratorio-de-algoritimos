nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
cal1 = (nota1 + nota2)/2

if cal1 > 9 and cal1 <= 10:
    print("A")

elif cal1 < 9 and cal1 >= 7.5:
    print("B")

elif cal1 < 7.5 and cal1 >= 6:
    print("C")

elif cal1 < 6 and cal1 >= 4:
    print("D")

else:
    print("E")
