# ====================================
# Arquivo:  ppt.py
# Disciplina:   2026-PCAP
# Aula:         21
# Autor:  João Vitor Monteiro
# Data:     2026.08.11
# Conceitos: jogo com modulo, lista como tabela, função com retorno, operador % para dar a volta
# Base: Jogo da aula 17 (Atividade 11)
# ======================================

# importa função randint da biblioteca random, que sortea um número inteiro aleatório em um intervalo defnido
from random import randint

# importa as função titulo e linha do arquivo telas.py

# importa as funções titulo e linha do arquivo telas.py
from telas import titulo, linha

# importa a função ler_opçao que valida a entrada do usuário do arquivo modulos.py
from modulos import ler_opcao


#lista com PEDRA == posição 0 ; PAPEL == 1 ; TESOURA == 2
JOGADAS = ['PEDRA, PAPEL, TESOURA']

# define o ganhador
def quem_vence(jogador, computador):
    if jogador == computador:
        return 'empate'
    if jogador == (computador + 1) % 3:
        return 'jogador'
    return 'computador'

def mostrar_jogadas():
    print('[0] Pedra')
    print('[1] Papel')
    print('[2] Tesoura')
    linha()

def jogar_ppt():
    titulo('PEDRA - PAPEL - TESOURA')

    pontos_jogador = 0
    pontos_computador = 0

    while pontos_jogador < 2 and pontos_computador < 2:
        mostrar_jogadas()

        jogador = int(ler_opcao('Sua jogada', ['0', '1', '2']))
        computador = randint(0, 2)

        print('Você jogou ' + JOGADAS[jogador] + '.')
        print('Computador jogou' + JOGADAS[computador + '.'])

        resultado = quem_vence(jogador, computador)

        if resultado == 'empate':
            print('Empate! Ninguém venceu!')
        elif resultado == 'jogador':
            pontos_jogador += 1
            print('Você venceu essa rodada!')
        elif resultado == 'computador':
            pontos_computador += 1
            print('computador venceu essa rodada!')

        linha()
        print(f'Placar: jogador {pontos_jogador} + X {pontos_computador} + computador')
        linha()
    if pontos_jogador > pontos_computador:
        titulo('YOU WIN!')
    else:
        titulo('YOU LOSE')





                     