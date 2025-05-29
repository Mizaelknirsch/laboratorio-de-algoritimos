def valor_0_40():
    
    qtd_laranjas = int(input("digite a quantidade que quer: "))
    if qtd_laranjas <= 12:
        valor = qtd_laranjas * 0.40
        print("o valor da compra fica : ", valor)
    elif qtd_laranjas > 12:
        desconto = qtd_laranjas * 0.25
        print("valor com desconto: ",desconto )

    
    


def main():
    valor_0_40()
   

main()
