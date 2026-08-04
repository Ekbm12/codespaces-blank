# '''
# Nome: João Vitor Monteiro
# Data: 02/07/2026
# '''

import random

# Numero

Numero_random = random.randint(1,5)

# palpite
dedos_jogador = int(input("Seu palpite (1 a 5)"))
dedos_maquina = random.choice

#jogada valida
opções = ["par, impar"]
if dedos_jogador not in opções:
    print("Jogada invalida")

print(10 % 2)
print(7 % 2)

#
soma = dedos_jogador + dedos_maquina
if soma % 2 == 0:
    print("par")
    
else:
    print("impar")    