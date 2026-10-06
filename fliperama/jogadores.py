# ====================================
# Arquivo:  jogadores.py
# Disciplina:   2026-PCAP
# Aula:         22
# Autor:  João Vitor Monteiro
# Data:     2026.08.24
# Conceitos:
# ======================================

from telas import titulo, linhas
from modulos import ler_opcao, ler_texto

def cadastrar_(jogadores):
    titulo('NOVO JOGADOR')

    apelido = input('Apelido (sem espacos): ').strip().lower()
    nome = input('Nome completo:').strip()


    novo = [apelido, nome, '0']
    jogadores.append(novo)

    print('Jogador ' + apelido + ' cadastrado.')
    linhas()



    jogadores = ['ana', 'Ana Souza', '0'], ['bel', 'Isabel Ramos', '0'] 

    cadastrar_(jogadores)
    cadastrar_(jogadores)
    listar(jogadores)
    print(jogadores)

    def listar(jogadores):
        titulo('JOGADORES CADASTRADOS')

    if len(jogadores) == 0:
        print('Nenhum jogador cadastro ainda.')
    else:
        for jogador in jogadores:
            print(jogador[0] + '|' +jogador[1]+'|' + jogador[2] + 'partidas')
            
            linhas()

def cadastrar(jogadores):
    titulo('NOVO JOGADOR')

    apelido = ler_texto('Apelido (sem espacos)').lower()
    nome = ler_texto('Nome completo')


def buscar(jogadores,apelido):
    for i in range(len(jogadores)):


def cadastrar(jogadores):
    titulo('NOVO JOGADOR')


def excluir(jogadores):
    listrar(jogadores)




