import json

# Leitura dos dados do arquivo JSON
with open("faturamento.json", "r") as f:
    faturamento_mensal = json.load(f)

# Cálculo do menor e maior faturamento diário
menor_faturamento = min(faturamento_mensal.values())
maior_faturamento = max(faturamento_mensal.values())

# Cálculo da média mensal de faturamento
dias_uteis = 0
total_faturamento = 0
for dia, faturamento in faturamento_mensal.items():
    if dia.startswith("d"):
        dias_uteis += 1
        total_faturamento += faturamento
media_mensal = total_faturamento / dias_uteis

# Cálculo do número de dias com faturamento acima da média mensal
dias_acima_media = 0
for faturamento in faturamento_mensal.values():
    if faturamento > media_mensal:
        dias_acima_media += 1

# Impressão dos resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
