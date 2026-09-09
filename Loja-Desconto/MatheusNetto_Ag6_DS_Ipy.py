# Entrada de dados do programa (Valor da compra)
valor = float(input("Digite o valor da compra em R$: "))
desconto = 0.0

# Processamento (Cálculo do desconto com base no valor da compra)
if valor <200:
    desconto = valor * 0.05
    #Dentro de cada condição, o programa calcula o desconto e imprime o valor do desconto e o preço total após o desconto. (Saída de dados)
    print(f"Desconto de 5%: R${desconto:.2f}. Preco total: R${valor-desconto:.2f}")
elif valor >= 200 and valor < 300:
    desconto = valor * 0.10
    print(f"Desconto de 10%: R${desconto:.2f}. Preco total: R${valor-desconto:.2f}")
else:
    desconto = valor * 0.15
    print(f"Desconto de 15%: R${desconto:.2f}. Preco total: R${valor-desconto:.2f}")