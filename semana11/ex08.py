ista = []
contador = 0
teste = 0
while contador < 5:
    try:
        i = int(input("digite um número: "))
        lista.append(i)
        contador += 1
    except:
        print("tente um número inteiro")
while True:
    try:
        n = int(input("digite um número para verificar se ele está na lista: "))
        break
    except:
        print("digite um número inteiro")
for i in lista:
    if n == i:
        teste = 1
if teste == 1:
    print("o número está na lista")
else:
    print("o número não está na lista")
