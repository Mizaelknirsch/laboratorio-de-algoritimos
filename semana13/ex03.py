def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True:
    entrada = input("Digite a temperatura em Celsius (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    try:
        celsius = float(entrada)
        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C equivalem a {fahrenheit}°F")
    except ValueError:
        print("Por favor, digite um número válido ou 'sair'.")
