
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
    print(f"Horário convertido: {h12}:{min:02d} {periodo}")

hora = int(input("Digite a hora (0-23): "))
minuto = int(input("Digite os minutos (0-59): "))

if 0 <= hora <= 23 and 0 <= minuto <= 59:
    h12, min_conv, periodo = converter_para_12h(hora, minuto)
    exibir_horario(h12, min_conv, periodo)
else:
    print("Hora ou minuto inválido.")
