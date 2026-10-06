# ====================================
# Arquivo:  placar.py
# Disciplina:   2026-PCAP
# Aula:         21
# Autor:  João Vitor Monteiro
# Data:     2026.08.24
# Conceitos:
# ======================================

ARQUIVO = 'placar.csv'
NOMES = ['Adivinhe o Numero', 'Pedra-papel-Tesoura']


def salva_placar(vezes):
    # o 'w' esvazia o arquivo e escreve tudo de novo.
    arquivo = open(ARQUIVO, 'w')
    for i in range(3):
        arquivo.write(NOMES[i] + ',' + str(vezes[i]) + '/n')
    arquivo.close()


def carrega_placar():
    arquivo = open(ARQUIVO, 'r')
    linhas = arquivo.readlines()
    arquivo.close()


    vezes = []
    for linha_lida in linhas:
        pedacos = linha_lida.strip().split(',')
        vezes.append(int(pedacos[1]))

    return vezes


from os.path import exists


def carregar_placar():
    # A primeira vez de todas: o arquivo ainda não existe.
    if not exists(ARQUIVO):
        return [0, 0, 0]

    arquivo = open(ARQUIVO, 'r')
