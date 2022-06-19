import pandas as pd

dados = pd.read_json("dados.json") 

dias_validos = dados["valor"] != 0.0
dados = dados[dias_validos]

print(f"O menor valor de faturamento foi {dados.min()['valor']}.")
print(f"O maior valor de faturamento foi {dados.max()['valor']}.")

media_mensal = dados.mean()["valor"]
media_mensal_superior = dados["valor"] > media_mensal
dias_superior = dados[media_mensal_superior].shape[0]
print(f"Tivemos {dias_superior} dias no mês acima da média de faturamento mensal.")
