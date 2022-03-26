import pandas as pd
from funcoes import *

df = pd.read_csv('br-capes-bolsistas-uab.csv', encoding="ISO-8859-1", delimiter=';')
pd.options.display.max_columns = None
pd.options.display.max_rows = None

init_menu = True
while init_menu:
    print('\nMENU')
    print('1) Consultar bolsa zero/Ano;')
    print('2) Codificar nome;')
    print('3) Consultar média atual;')
    print('4) Ranking valoresde bolsa;')
    print('5) Sair do programa.')

    escolha = int(input('Digite a escolha desejada:'))
    if escolha not in [1, 2, 3, 4, 5]:
        print('Escolha inválida, tente novamente.')

    if escolha == 1:
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

    if escolha == 2:
        # Questão 2: Codificar o nome do bolsista

        # transformar dados em novo DataFrame,
        # pegar apenas colunas necessárias
        df_questao2 = df[['AN_REFERENCIA', 'NM_ENTIDADE_ENSINO', 'VL_BOLSISTA_PAGAMENTO']]

        # input do nome e criar uma variavel para checar se é válido
        busca_nome = str(input('Nome (inteiro) do bolsista a codificar: ').upper())
        df_checar_vazio = df.loc[df['NM_BOLSISTA'] == busca_nome]

        # em casos de nome inválido, o DataFrame resultante
        # retorna vazio pois nao achou nenhuma entrada -
        # a funcao "empty" do pandas permite checar se
        # um DataFrame está vazio ou não
        if df_checar_vazio.empty:
            print('Nome inválido, tente novamente.')
        else:
            # usar funçoes para converter o nome
            conv_nome1 = separa_nome(busca_nome)
            conv_nome2 = codifica_nome(conv_nome1)
            conv_nome3 = converte_lista(conv_nome2)

            # criar coluna para nome codificado
            df_questao2.insert(0, 'NM_CODE', conv_nome3)

            print(df_questao2[df['NM_BOLSISTA'] == busca_nome])
            print(conv_nome3)

    if escolha == 3:
        # Questão 3: fazer média das bolsas de um dado ano

        # transformar dados em novo DataFrame,
        # pegar apenas colunas necessárias
        df_questao3 = df[['AN_REFERENCIA', 'VL_BOLSISTA_PAGAMENTO']]
        ano_calcular = int(input('Selecione o ano desejado:'))

        # checar se input é válido ou não
        if ano_calcular in [2013, 2014, 2015, 2016]:
            print(df_questao3.loc[df_questao3['AN_REFERENCIA'] == ano_calcular]['VL_BOLSISTA_PAGAMENTO'].mean())
        else:
            print('Ano de busca inválido!')
            print('Tente: 2013, 2014, 2015 ou 2016')

    if escolha == 4:
        # Questao 4: os 3 alunos com maior valor de bolsa
        # e os 3 com menor valor de bolsa

        print('Mostrar os maiores ou menores?')
        maior_ou_menor = int(input('Digite 1 (maior) ou 2 (menor):'))

        if maior_ou_menor not in [1, 2]:
            print('Escolha inválida, tente novamente')
        elif maior_ou_menor == 1:
            print(df.sort_values('VL_BOLSISTA_PAGAMENTO', ascending=False).head(3)[
                      ['NM_BOLSISTA', 'VL_BOLSISTA_PAGAMENTO']])
        elif maior_ou_menor == 2:
            print(df.sort_values('VL_BOLSISTA_PAGAMENTO', ascending=True).head(3)[
                      ['NM_BOLSISTA', 'VL_BOLSISTA_PAGAMENTO']])

    if escolha == 5:
        print("FIM")
        init_menu = False
