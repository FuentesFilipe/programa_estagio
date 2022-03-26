import pandas as pd

df = pd.read_csv("br-capes-bolsistas-uab.csv", encoding="ISO-8859-1", delimiter=";")

# Questao 4: os 3 alunos com maior valor de bolsa
# e os 3 com menor valor de bolsa

# print(df['VL_BOLSISTA_PAGAMENTO'].nlargest(3))
# print(df['VL_BOLSISTA_PAGAMENTO'].nsmallest(3))


print(df.sort_values('VL_BOLSISTA_PAGAMENTO', ascending=False).head(3)[['NM_BOLSISTA', 'VL_BOLSISTA_PAGAMENTO']])
print(df.sort_values('VL_BOLSISTA_PAGAMENTO', ascending=True).head(3)[['NM_BOLSISTA', 'VL_BOLSISTA_PAGAMENTO']])