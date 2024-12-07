# Função para escolher o modelo da camiseta
def escolha_modelo():
    while True:
        camiseta = input(">>").strip().upper()
        if camiseta == "MCS":
            preco = 1.80
            modelo = "Manga Curta Simples"
            return preco, modelo
        elif camiseta == "MLS":
            preco = 2.10
            modelo = "Manga Longa Simples"
            return preco, modelo
        elif camiseta == "MCE":
            preco = 2.90
            modelo = "Manga Curta Com Estampa"
            return preco, modelo
        elif camiseta == "MLE":
            preco = 3.20
            modelo = "Manga Longa Com Estampa"
            return preco, modelo
        else:
            print("Escolha inválida, entre com o modelo novamente.")  # Caso a opção escolhida for diferente das apresentadas


# Função para escolher a quantidade de camisetas          
def num_camisetas():
    while True:
        try:
            quantidade = int(input("Qual a quantidade de camisetas? "))
            if quantidade < 20:
                desconto = 0
            elif 20 <= quantidade < 200:
                desconto = 0.05
            elif 200 <= quantidade < 2000:
                desconto = 0.07
            elif 2000 <= quantidade <= 20000:
                desconto = 0.12
            elif quantidade > 20000:
                print("Não aceitamos tantas camisetas de uma vez.\nPor favor, entre com o número de camisetas novamente.")
                continue  # Solicita a quantidade novamente
            return desconto, quantidade  # Retorna o desconto e a quantidade
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")


# Função utilizada para calcular o frete
def calcular_frete():
    while True:
        try:
            print("Escolha o tipo de frete: ")
            print("1 - Frete por transportadora - R$ 100.00")
            print("2 - Frete por sedex - R$ 200.00")
            print("0 - Retirar pedido na fábrica - R$ 0.00")
            escolha = int(input(">>"))
            if escolha == 1:
                return 100
            elif escolha == 2:
                return 200
            elif escolha == 0:
                return 0
            else:
                print("Opção incorreta! Tente novamente. ")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")  # Caso a opção escolhida for diferente das apresentadas


# Programa Principal 
print("Bem-vindos à Fábrica de Camisetas do Adolpho Evaristo Corrêa Neto")
print("\nEntre com o Modelo Desejado:")
print("MCS - Manga Curta Simples ")
print("MLS - Manga Longa Simples ")
print("MCE - Manga Curta Com Estampa ")
print("MLE - Manga Longa Com Estampa \n")

preco, modelo = escolha_modelo()
desconto, quantidade = num_camisetas()  # Armazena ambos os valores corretamente
frete = calcular_frete()

# Aplica o desconto ao preço total das camisetas
total_camisetas = preco * quantidade * (1 - desconto)

# Calcula o valor total do pedido com o frete
total = total_camisetas + frete

print(f"Total: R$ {total:.2f}  ({modelo}: R$ {preco} * Quantidade: {quantidade} (Desconto: {desconto*100:.2f}%) + Frete: R$ {frete})\n")