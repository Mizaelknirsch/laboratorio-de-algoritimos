v = 0
idade = 0 
altura = 0 
contador = 0 
somaidade = 0
somaaltura = 0
while v != 3:
    print("1 cadastrar pessoa")
    print("2 mostrar média parcial da altura e idade")
    print("3 sair")
    v = int(input("digiite uma opção: "))
    if v == 1:
        idade = int(input("digite a sua idade: "))
        altura = float(input("digite a sua altura: "))
        somaaltura = somaaltura + altura
        somaidade = somaidade + idade
        contador += 1
    elif v == 2:
        print("media de idade é", somaidade / contador)
        print("media de altura é", somaaltura / contador)
