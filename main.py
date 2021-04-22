def analisador_de_lista(lista):
    """
    Função com objetivo de identificar listas com itens repetidos.
    :param lista: recebe uma array, com x strings.
    :return: True, caso algum item da array for igual a outro. False, caso todos os itens da array forem diferentes.
    """
    d = 1
    for a in range(0, len(lista) - 1):
        for c in range(d, len(lista)):
            if lista[a] == lista[c]:
                return True
        d += 1
    return False


def avoids(lista, arquivo):
    """
    Função cujo objetivo é calcular o número de palavras não exluídas. Com base o banco de dados(arquivo) e com base as 5 letras que
    as palavras não podem ter(lista). A função analisa todas as palavras do arquivo, e para cada palavra, analisa-se se alguma letra dessa
    palavras também existe na lista de letras proibidas.
    :param lista: array com 5 caractéres.
    :param arquivo: banco de dados.
    :return: o número de palavras não excluídas em detrimento da restrição: as 5 letras.
    """
    palavras_words = open(arquivo)

    palavra_sem_letra_proibida = 0
    total_de_palavras = 0

    for linhas in palavras_words:
        total_de_palavras += 1
        a = linhas.replace('\n', '')
        second_break = False

        for letras_da_palavra in range(0, len(a)):
            for letra_da_lista in range(0, len(lista)):
                if lista[letra_da_lista] == a[letras_da_palavra]:
                    second_break = True
                    break
            if second_break == True:
                break
        if second_break == False:
            palavra_sem_letra_proibida += 1

    return int(palavra_sem_letra_proibida)


def dectector_de_listas_iguais(lista_ascii, lista_temp):
    """
    Função cujo objetivo é receber inúmeras listas(lista_temp) e cadastrar progressivamente a soma dos números ASCII deles, assim, podemos
    restrigir quais listas vão ser analisdas mais pra frente no programa.
    :param lista_ascii: lista com número ASCII de listas já analisados.
    :param lista_temp: lista temporária analisada.
    :return: caso a lista_temp tenha a soma dos números ASCII já cadastrada na lista_ascii, significa que essa lista já foi analisada antes,
    assim retornamos True; caso contrário, retonamos a soma ASCII da lista_temp, para ser cadastrada na lista, fora da função.
    """
    num_ascii = 0
    for c in range(0, len(lista_temp)):
        num_ascii += ord(lista_temp[c])

    for itens_em_ascii in range(0, len(lista_ascii)):
        if lista_ascii[itens_em_ascii] == num_ascii:
            return True
    return num_ascii


"""
------------------
PROGRAMA PRINCIPAL
------------------
No programa principal faz-se o uso das funções dectector_de_listas_iguais() e analisador_de_lista() para restringir a quantidade de
arrays que realmente deve ser analisadas pela função avoid(), e não são arrays repetidads ou arrays iguais de caractéres trocados.

O programa escreve sempre que acha uma lista que exclúi um valor mínimo até o momento, além do número de palavras não excluídas da base de
dados.

No final da execução, o programa escreve a lista que excluiu o menor número de palavras, e o número de palavras não excluídas.
"""
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lista_temp = ['', '', '', '', '']
num_max_palavras = 0
lista_ascii = []

lista_com_menor_exclusao_de_palavras = []

for primeira_letra in range(0, len(lista)):
    for segunda_letra in range(0, len(lista)):
        for terceira_letra in range(0, len(lista)):
            for quarta_letra in range(0, len(lista)):
                for quinta_letra in range(0, len(lista)):
                    lista_temp[0] = lista[primeira_letra]
                    lista_temp[1] = lista[segunda_letra]
                    lista_temp[2] = lista[terceira_letra]
                    lista_temp[3] = lista[quarta_letra]
                    lista_temp[4] = lista[quinta_letra]

                    if not analisador_de_lista(lista_temp):
                        if not dectector_de_listas_iguais(lista_ascii, lista_temp):
                            lista_ascii.append(dectector_de_listas_iguais(lista_ascii, lista_temp))
                            if lista_temp == ['a', 'b', 'c', 'd', 'e']:
                                lista_com_menor_exclusao_de_palavras = lista_temp[:]
                                num_max_palavras = avoids(lista_com_menor_exclusao_de_palavras, 'words.txt')
                            else:
                                a = avoids(lista_temp, 'words.txt')
                                if a > num_max_palavras:
                                    num_max_palavras = a
                                    lista_com_menor_exclusao_de_palavras = lista_temp[:]
                                    print(f'Encontrei uma lista melhor... \nLISTA : '
                                          f'{lista_com_menor_exclusao_de_palavras}\n'
                                          f'PALAVRAS NÃO EXCLUÌDAS {num_max_palavras}')
                                    print('-'*30)

print(f'MELHOR LISTA: {lista_com_menor_exclusao_de_palavras}, número de palavras não excluidas: {num_max_palavras}')
