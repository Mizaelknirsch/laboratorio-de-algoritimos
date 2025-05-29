def somaImposto(taxaImposto, custo):
    custo_final = custo + (custo * taxaImposto / 100)
    return custo_final

taxa = float(input("Digite a taxa de imposto (%): "))
custo = float(input("Digite o custo do item: R$ "))

custo_com_imposto = somaImposto(taxa, custo)

print(f"Custo com imposto: R$ {custo_com_imposto:.2f}")
