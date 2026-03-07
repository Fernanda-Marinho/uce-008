a = int(input("Digite um número inteiro: "))
b = int(input("Digite um número inteiro: "))
c = int(input("Digite um número inteiro: "))

if (b < a < c) or (c < a < b):
    print(a)
else:
    if (a < b < c) or (c < b < a):
        print(b)
    else:
        print(c)