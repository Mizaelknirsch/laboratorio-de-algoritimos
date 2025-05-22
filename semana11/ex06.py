n = []
contador = 0
while contador < 6:
    try:
        i = float(input("digite um número: "))
        n.append(i)
        contador += 1
    except:
        print("tente um número válido")
while True:
    try:
        m = float(input("digite o multiplicador: "))
        break
    except:
        print("tente um número válido")
for i in n:
    print(f"{i} X {m} = {i * m}")
