lista1 = []
lista_pares = []


for i in range(1,11):
    valores = int(input("digite os numeros do valores: "))
    lista1.append(valores)

print(f"lista coompleta: {lista1}")


for v in lista1: 
    if v % 2 == 0:
        lista_pares.append(v)
            

print(f"lista de pares : {lista_pares}")
