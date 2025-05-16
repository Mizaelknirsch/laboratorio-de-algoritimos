lista = []

valor_maior100 = []


for i in range(10):
    valores = int(input("Digite os valores: "))
    if valores <= 100:
        lista.append(valores)
        print(f"valores abaio de 100: {lista}")
      
    else: 
        valor_maior100.append(valores)

        print(f"maiore que 100 {valor_maior100}")
