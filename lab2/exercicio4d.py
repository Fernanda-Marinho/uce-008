preco_sem_desconto = float(input("Digite o preço do produto: "))

if preco_sem_desconto >= 200.00:
    #valor_final = preco_sem_desconto * 0.95
    valor_final = (preco_sem_desconto - (5/100) * preco_sem_desconto) 
else:
    valor_final = preco_sem_desconto

print(f"{valor_final:.2f}")