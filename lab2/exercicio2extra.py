num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

produto = num1 * num2

if produto % 7 == 0:
    print(num1 + num2)
else:
    print(num2 - num1)