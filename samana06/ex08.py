contador_A = 0
contador_B = 0
contador_C = 0
contador = 1
while contador <= 10:
    elevador = input(f"Morador {contador}, qual elevador você usa com mais frequência? (A/B/C): ")
    if elevador == 'A' or elevador == 'a':
        contador_A += 1
    elif elevador == 'B' or elevador == 'b':
        contador_B += 1
    elif elevador == 'C' or elevador == 'c':
        contador_C += 1
    contador += 1
porcentagem_A = (contador_A / 10) * 100
porcentagem_B = (contador_B / 10) * 100
porcentagem_C = (contador_C / 10) * 100
print(f"Total de pessoas que usam o elevador A: {contador_A} ({porcentagem_A:.2f}%)")
print(f"Total de pessoas que usam o elevador B: {contador_B} ({porcentagem_B:.2f}%)")
print(f"Total de pessoas que usam o elevador C: {contador_C} ({porcentagem_C:.2f}%)")
