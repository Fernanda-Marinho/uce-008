n = int(input("Digite um número inteiro de dois dígitos: "))

primeiro_digito = n // 10
segundo_digito = n % 10

if primeiro_digito == segundo_digito:
    print("DÍGITOS IGUAIS")
else:
    print("DÍGITOS DIFERENTES")