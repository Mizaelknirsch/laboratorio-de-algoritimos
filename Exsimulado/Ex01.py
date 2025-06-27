def comparar(arr1, arr2):
    a = set(arr1)
    b = set(arr2)
    comuns = a & b
    final = [n for n in comuns if n > 10]
    return final

def main():
    lista1 = [3, 8, 30, 12, 18, 25]
    lista2 = [4, 5, 12, 18, 30, 30]
    resposta = comparar(lista1, lista2)

    if resposta:
        print("Números em comum maiores que 10:", resposta)
    else:
        print("Não há números em comum maiores que 10.")

main()
