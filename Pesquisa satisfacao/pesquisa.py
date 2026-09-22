excelente = 0
bom = 0
ruim = 0
# Entrada de dados
for i in range(1,51):
	nome = input("Digite o seu nome:")
	idade = input("Digite a sua idade:")
	pesquisa = input("Qual o seu nivel de satisfação com o atendimento da loja? Pressione 1 para Excelente, 2 para Bom e 3 para Ruim: ")
# Validação da pesquisa
	while pesquisa != "1" and pesquisa != "2" and pesquisa != "3":
		print("Opção incorreta, digite uma das opções disponíveis")
		pesquisa = input("Pressione 1 para Excelente, 2 para Bom e 3 para Ruim: ")
	if pesquisa == "1":
		excelente += 1
	elif pesquisa == "2":
		bom += 1
	else:
		ruim += 1
# Resultados
print(f"Nós tivemos {excelente:.0f} repostas excelentes!")
print(f"Nós tivemos {ruim:.0f} repostas negativas, rever como estamos tratando nossos clientes!")