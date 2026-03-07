percurso = float(input("Digite o percurso em km: "))
tipo_carro = input("Digite o tipo do carro (A ou B): ")

if tipo_carro == "A": # 8 km/l
    consumo = percurso / 8
else: # 12 km/l
    consumo = percurso / 12

print(f"{consumo:.2f}")