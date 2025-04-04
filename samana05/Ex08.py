lado1 = float(input("digite o primeiro lado do triangulo: "))
lado2 = float(input("digite o segundo lado do triangulo: "))
lado3= float(input("digite o terceiro lado do triangulo: "))

if lado1 and lado2 == lado3:
    print("triangulo equilátero")

elif lado1 == lado2:
    print("tiangulo Isósceles")

elif lado2== lado3:
    print("tiangulo Isósceles")

elif lado1 == lado3:
    print("tiangulo Isósceles")

else:
    print("triangulo Escaleno")
