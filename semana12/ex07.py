def converter_para_12h(hora, minuto):
    if hora == 0:
        return 12, minuto, "A.M."
    elif 1 <= hora < 12:
        return hora, minuto, "A.M."
    elif hora == 12:
        return 12, minuto, "P.M."
    else:
        return hora - 12, minuto, "P.M."


def exibir_horario(h12, min, periodo):
    print(f"Horário convertido: {
