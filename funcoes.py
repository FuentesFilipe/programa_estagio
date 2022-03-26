from string import ascii_uppercase as letras


def codifica_nome(nome_lista: list) -> list:
    tamanho_lista = len(nome_lista)
    lista_code = []
    for i in range(tamanho_lista):
        nome_start = nome_lista[i]

        # verificar se parametro tem 3 letras
        # se tiver, execute passo 1 e 3 apenas
        if len(nome_start) == 3:
            penultimo_char = len(nome_start) - 1
            passo01 = nome_start[-1] + nome_start[1:penultimo_char] + nome_start[0]

            passo03 = ""
            for char in passo01:
                if char in letras:
                    passo03 = passo03 + letras[(letras.index(char) + 1) % len(letras)]
                else:
                    passo03 += char
            lista_code.append(passo03)

            # verificar se parametro tem 2 letras
            # se tiver, execute passo 1 e 3 apenas
            if len(nome_start) == 2:
                passo001 = nome_start[-1] + nome_start[0]

                passo003 = ""
                for char in passo001:
                    if char in letras:
                        passo003 = passo003 + letras[(letras.index(char) + 1) % len(letras)]
                    else:
                        passo003 += char
                lista_code.append(passo003)

        else:
            # 1) trocar o primeiro char pelo ultimo
            penultimo_char = len(nome_start) - 1
            passo1 = nome_start[-1] + nome_start[1:penultimo_char] + nome_start[0]

            # 2) inverter a string
            passo2 = passo1[::-1]

            # 3) converter todos os chars para
            # o proximo char no alfabeto (ex: A->B, C->D, ...)
            passo3 = ""
            for char in passo2:
                if char in letras:
                    passo3 = passo3 + letras[(letras.index(char) + 1) % len(letras)]
                else:
                    passo3 += char
            lista_code.append(passo3)
    return lista_code


# separar nome em uma lista, codificaçao vai ser diferente
# caso nome tenha 3 caracteres no total

def separa_nome(nome_bruto: str) -> list:
    nome_lista = nome_bruto.split(" ")
    return nome_lista


# pega o nome codificado em formato lista
# e converte de volta para uma string

def converte_lista(lista_code: list) -> str:
    resultado = " ".join(lista_code)
    return resultado
