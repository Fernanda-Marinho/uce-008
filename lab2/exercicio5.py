n = int(input("Digite um número de 3 dígitos: "))
restante = n % 100
if n % restante == 0:
    print("SIM")
else:
    print("NÃO")