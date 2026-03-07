preco = float(input("Digite o preço do produto: "))
pagamento = float(input("Digite o valor pago pelo cliente: "))

if preco > pagamento:
    falta = preco - pagamento
    print(f"Falta {falta:.1f}")
else:
    troco = pagamento - preco
    print(f"Troco de {troco:.1f}")