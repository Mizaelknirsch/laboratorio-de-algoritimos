preco= float(input("digite o valor da roupa:"))

print("se for feito em 2 vezes deve ser cobrado 5%  de juros. ")
print("se for feito em 3 vezes deve ser cobrado 10%  de juros.")
vezes = float(input('Digite quantas vezes queres fazer(liberado em 2 ou 3 vezes ): '))

if vezes == 1:
    print("valor sem juros: ", preco)

elif vezes == 2:
    preco2 = preco * 1.05
    print("valor com 5% de juros: ", preco2)

elif vezes == 3:
    preco3 = preco * 1.10
    print("valor com 10% de juros: ", preco3)

else:
    print("valor indisponmivel para parcelar!!")
