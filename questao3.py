import pandas as pd

df = pd.read_csv("br-capes-bolsistas-uab.csv", encoding="ISO-8859-1", delimiter=";")

# Questão 3: fazer média das bolsas de um dado ano
df_questao3 = df[['AN_REFERENCIA', 'VL_BOLSISTA_PAGAMENTO']]
ano_calcular = 2015

print(df_questao3.loc[df_questao3['AN_REFERENCIA'] == ano_calcular]['VL_BOLSISTA_PAGAMENTO'].mean())
