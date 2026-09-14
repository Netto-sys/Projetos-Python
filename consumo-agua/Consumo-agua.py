# Entrada de dados do morador
imovel = input('Informe o tipo de imovel(opções esperadas: "comercial", "casa" ou "apartamento"): ')
# Verificando se o tipo de imóvel é válido
if imovel not in ["comercial", "casa", "apartamento", "Comercial", "Casa", "Apartamento"]:
    print('Tipo de imóvel inválido. Por favor, insira "comercial", "casa" ou "apartamento".')
# Se o tipo de imóvel for válido, solicitar o consumo mensal de água
else:
    consumo = float(input("Informe o consumo mensal de água em metros cúbicos ( 𝑚 3 ): "))
# Avaliando o consumo de água com base no tipo de imóvel (saída de acordo com o consumo e o tipo de imóvel)
    match imovel:
        case "comercial"|"Comercial":
             print(" Tarifa comercial aplicada - consulte o plano corporativo")
        case "apartamento"|"Apartamento" if consumo < 10:
             print("Consumo econômico – excelente controle de água!")
        case "Apartamento"|"Casa"|"apartamento"|"casa" if consumo <= 25:
             print("Consumo moderado – dentro do padrão residencial.")
        case "apartamento"|"Apartamento"|"casa"|"Casa" if consumo > 25:
             print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

