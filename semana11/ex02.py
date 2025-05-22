lista = []
listab = []
contador = 0
while contador < 5:
    try:
        i = float(input("digite um número: "))
        lista.append(i)
        contador += 1
    except:
        print("tente digitar um número válido")
for i in range(len(lista) - 1, -1, -1):
    f = lista[i]
    listab.append(f)
print(listab)
