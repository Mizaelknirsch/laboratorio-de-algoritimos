valor_maior30 = []
valor_menor30 = []

for i in range(8):
    valores = int(input("Digite os numeros: "))
    if valores > 30:
        valor_maior30.append(valores)
        print(f"maior que 30: {valor_maior30}")
        
       

    
    else:
        valor_menor30.append(valores)
        print(f"valor menor que 30: {valor_menor30}")

soma_maior30 = 0

for y in  valor_maior30:
    soma_maior30 += y

somatotal = 0
for v in valor_menor30 + valor_maior30:
    somatotal += v



 
print(f"soma dos 30: {soma_maior30}")
print(f"soma de tudo: {somatotal}")
