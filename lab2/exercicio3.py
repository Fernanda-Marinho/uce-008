escala = input("Digite a escala (C para Celsius, F para Fahrenheit): ")
temp = float(input("Digite a temperatura: "))

#if escala.lower() == "c":
if escala == "C": #converte celcius para fahrenheit
    resultado = (temp * 9/5) + 32
    print(f"{resultado:.1f}")
else: #converte fahrenheit para celcius
    resultado = (5/9) * (temp - 32)
    print(f"{resultado:.1f}")