numeros = []
contador = 0
soma = 0
while contador < 5:
    try:
        i = float(input("digite um número: "))
        numeros.append(i)
        contador += 1
    except:
        print("digite um número válido")
for i in numeros:
    soma += i
print(f"a média dos seguintes números {numeros} é {soma / len(numeros)}")
