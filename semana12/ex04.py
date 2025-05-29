def ler_notas():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    return notas


def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"


notas = ler_notas()
media = calcular_media(notas)
situacao = verificar_situacao(media)

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
