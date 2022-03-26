import pandas as pd


df = pd.read_csv('br-capes-bolsistas-uab.csv', encoding='ISO-8859-1', delimiter=';')
limited_df = df.head(10)

# Questao 1: Achar o primeiro bolsista do ano digitado

# transformar dados em novo DataFrame,
# pegar apenas colunas necessárias
df_questao1 = df[['NM_BOLSISTA', 'CPF_BOLSISTA', 'NM_ENTIDADE_ENSINO', 'VL_BOLSISTA_PAGAMENTO']]

# enxergar input do usuario como um inteiro
ano_query = int(input('Selecione o ano desejado:'))

# checar se input é válido ou não
if ano_query in [2013, 2014, 2015, 2016]:
    print(df_questao1[df['AN_REFERENCIA'] == ano_query].iloc[0])
else:
    print('Ano de busca inválido!')
    print('Tente: 2013, 2014, 2015 ou 2016')
