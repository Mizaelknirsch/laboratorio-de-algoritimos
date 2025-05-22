a = []
b = []
c = []
contador = 0
while contador < 5:
    try:
        i = int(input(f"digite o {contador+1}º número da primeira lista: "))
        a.append(i)
        contador += 1
    except:
        print("tente um número inteiro")
contador2 = 0
while contador2 < 5:
    try:
        i = int(input(f"digite o {contador2+1}º número da segunda lista: "))
        b.append(i)
        contador2 += 1
    except:
        print("tente um número inteiro")
produto = 0
for i in range(len(a)):
    produto = a[i] * b[i]
    c.append(produto)
print("o produto de elemento a elemento de cada lista é:")
print(c)
