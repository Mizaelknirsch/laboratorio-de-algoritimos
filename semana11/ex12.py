lista = []
contador = 0
teste = 0
while contador < 15:
    try:
        numero = int(input(f"Digite o {len(lista) + 1}º número: "))

        if numero in lista:
            print("Número já está na lista. Digite um valor diferente")
        else:
            lista.append(numero)
            contador += 1
    except:
        print("digite um número inteiro válido.")
print(lista)
