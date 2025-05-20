# Escolha do período
print("Selecione o período de análise:")
print("1 - Mensal")
print("2 - Trimestral")
print("3 - Anual")
opcao = input("Digite o número correspondente ao período: ")

if opcao == "1":
    multiplicador = 1
    periodo = "Mensal"
elif opcao == "2":
    multiplicador = 3
    periodo = "Trimestral"
elif opcao == "3":
    multiplicador = 12
    periodo = "Anual"
else:
    print("Opção inválida. Usando período mensal por padrão.")
    multiplicador = 1
    periodo = "Mensal"

# Espaço total disponível no estoque (m³)
espaco_disponivel = float(input("\nDigite o espaço total disponível em m³ para armazenamento: "))

# Dados do aluguel
custo_aluguel_m3 = float(input("\nDigite o valor do aluguel por m³ (ex: 10): "))
aluguel_minimo = float(input("Digite o valor mínimo do aluguel (ex: 100): "))
aluguel_maximo = float(input("Digite o valor máximo do aluguel (digite 0 se não houver): "))

# Lista de produtos
produtos = []

while True:
    print("\n--- Cadastro de Produto ---")
    nome = input("Digite o nome do produto: ")
    custo = float(input("Digite o custo de compra: "))
    venda = float(input("Digite o valor de venda: "))
    volume = float(input("Digite o volume em m³ de uma unidade: "))
    demanda_mensal = int(input("Digite a demanda MENSAL (quantidade prevista de venda): "))
    minimo_mensal = int(input("Digite a quantidade mínima MENSAL obrigatória (ex: contrato ou venda certa): "))
    
    demanda_total = demanda_mensal * multiplicador
    minimo_total = minimo_mensal * multiplicador
    lucro_unitario = venda - custo
    lucro_por_m3 = lucro_unitario / volume if volume > 0 else 0

    produto = {
        "nome": nome,
        "custo": custo,
        "venda": venda,
        "lucro_unitario": lucro_unitario,
        "volume": volume,
        "demanda": demanda_total,
        "minimo": minimo_total,
        "lucro_por_m3": lucro_por_m3,
        "alocado": 0  # será preenchido depois
    }

    produtos.append(produto)

    continuar = input("Deseja adicionar outro produto? (s/n): ").lower()
    if continuar != "s":
        break

# Reservar espaço para o mínimo obrigatório de cada produto
espaco_restante = espaco_disponivel
for p in produtos:
    volume_necessario = p["volume"] * p["minimo"]
    if volume_necessario <= espaco_restante:
        p["alocado"] = p["minimo"]
        espaco_restante -= volume_necessario
    else:
        maximo_possivel = int(espaco_restante // p["volume"])
        p["alocado"] = maximo_possivel
        espaco_restante -= maximo_possivel * p["volume"]

# Ordena os produtos por lucro por m³ (desc)
produtos.sort(key=lambda p: p["lucro_por_m3"], reverse=True)

# Alocar espaço restante maximizando o lucro
for p in produtos:
    restantes_possiveis = p["demanda"] - p["alocado"]
    max_unidades = int(espaco_restante // p["volume"])
    adicionais = min(restantes_possiveis, max_unidades)
    p["alocado"] += adicionais
    espaco_restante -= adicionais * p["volume"]
    if espaco_restante <= 0:
        break

# Cálculo de resultados
print(f"\nMelhor alocação encontrada para o período {periodo}:")
lucro_total = 0
espaco_usado = 0
mais_lucrativo = ""
maior_lucro = -1

for p in produtos:
    quantidade = p["alocado"]
    lucro = quantidade * p["lucro_unitario"]
    volume_total = quantidade * p["volume"]
    print(f"{p['nome']}: {quantidade} unidades | Lucro: R$ {lucro:.2f} | Espaço usado: {volume_total:.2f} m³")
    lucro_total += lucro
    espaco_usado += volume_total
    if lucro > maior_lucro:
        maior_lucro = lucro
        mais_lucrativo = p["nome"]

# Custo da armazenagem
custo_armazenagem = espaco_usado * custo_aluguel_m3
if custo_armazenagem < aluguel_minimo:
    custo_armazenagem = aluguel_minimo
elif aluguel_maximo > 0 and custo_armazenagem > aluguel_maximo:
    custo_armazenagem = aluguel_maximo

lucro_liquido = lucro_total - custo_armazenagem

# Resultados finais
print(f"\nEspaço utilizado: {espaco_usado:.2f} m³ de {espaco_disponivel} m³ disponíveis")
print(f"Lucro total bruto: R$ {lucro_total:.2f}")
print(f"Custo de armazenagem: R$ {custo_armazenagem:.2f}")
print(f"Lucro líquido final: R$ {lucro_liquido:.2f}")
print(f"O produto mais vantajoso na alocação foi: {mais_lucrativo}")