dia_da_semana = int(input("Digite um número de 1 a 7: "))

if dia_da_semana >= 2 and dia_da_semana <= 6:
    print("Dia útil")
elif dia_da_semana == 1 or dia_da_semana == 7:
    print("Fim de semana")
else:
    print("Valor inválido")