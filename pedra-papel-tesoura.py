#'''
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAP)
# Projeto : Jogo "Pedra-Papel-Tesoura
# Arquivo : pedra-papel-tesoura.py
# Autor : João Vitor Monteiro
# Data : 16/06/2026
#'''

import random

# Opções:

Opções = ["pedra", "papel", "tesoura"]
pontos_jogador = 0
pontos_computador = 0

for rodada in range(1, 6):
    print("--- Rodada", rodada, "---")



jogada_computador = random.choice(Opções)

#jogada do jogador:
entrada =input("Jogar (pedra, papel ou tesoura)")
jogada_jogador = entrada.lower().strip()


# Bloquear opções aleatorias e indentificar empates,vitorias e derrotas

if jogada_jogador not in Opções:
    print ("Por favor jogue APENAS a opções mostradas")    
elif jogada_jogador == jogada_computador:
    print("Empatou!")
# Vitorias

elif jogada_jogador == "pedra" and jogada_computador == "tesoura":

    print("Você ganhou por quebrar a tesoura com a pedra!")

    pontos_jogador = pontos_jogador + 1

elif jogada_jogador == "papel" and jogada_computador == "pedra":

    print("Você ganhou cobrindo a pedra com o papel.")

    pontos_jogador = pontos_jogador + 1
elif jogada_jogador == "tesoura" and jogada_computador == "papel":

    print("Você ganhou cortando o papel com a tesoura.")

    pontos_jogador = pontos_jogador + 1

# Derrotas    

elif jogada_jogador == "pedra" and jogada_computador == "papel":
    
    print("Você perdeu,pois papel cobre a pedra")

    pontos_computador = pontos_computador + 1

elif jogada_jogador == "papel" and jogada_computador == "tesoura":   

    print("Você perdeu,pois tesoura corta papel")

    pontos_computador = pontos_computador + 1

# Placar final                       
print("Placar final = Voçê:", pontos_jogador, "| Computador:", pontos_computador)





