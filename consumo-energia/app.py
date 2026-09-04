# Programa de calculo de consumo de energia
# Autor: Netto

# Entrada
aparelho = input("Digite o nome do aparelho(ex.: Microondas): ")
potencia = float(input("Informe a potencia do aparelho em watts(W): "))
tempohoras = float(input("Informe o tempo de uso diário do aparelho em horas(h): "))

# Processamento
consumomensal = (potencia * tempohoras* 30) / 1000
custo = consumomensal * 0.75

# Saida 
print(f"Aparelho: {aparelho}")
print(f"Consumo Mensal: {consumomensal:.2f} kWh/mês")
if custo > 200:
    print(f"O custo mensal do {aparelho} é de R$ {custo:.2f}, cuidado com a conta de luz!")
else:
    print(f"O custo mensal do {aparelho} é de R$ {custo:.2f}, está dentro do esperado.")