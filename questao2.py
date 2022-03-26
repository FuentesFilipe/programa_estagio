import pandas as pd
from funcoes import *


df = pd.read_csv("br-capes-bolsistas-uab.csv", encoding="ISO-8859-1", delimiter=";")

pd.options.display.max_columns = None
pd.options.display.max_rows = None

# Questão 2: Codificar o nome do bolsista

# transformar dados em novo DataFrame,
# pegar apenas colunas necessárias
df_questao2 = df[['AN_REFERENCIA', 'NM_ENTIDADE_ENSINO', 'VL_BOLSISTA_PAGAMENTO']]

# string teste: "CAROLINE ALCANTARA DUARTE"
busca_nome = str(input("Nome (inteiro) do bolsista a codificar: ").upper())

# usar funçoes para converter o nome
conv_nome1 = separa_nome(busca_nome)
conv_nome2 = codifica_nome(conv_nome1)
conv_nome3 = converte_lista(conv_nome2)

# criar coluna para nome codificado
df_questao2.insert(0, 'NM_CODE', conv_nome3)

print(df_questao2[df['NM_BOLSISTA'] == busca_nome])
print(conv_nome3)
