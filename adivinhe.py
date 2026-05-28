# '''
# Disciplina : Pensamento Computacional, Algoritimos e Programação (PCAC)
# Projeto : Jogo "Adivinhe o Número"
# Arquivo : adivinhe.py
# Autor   : João Vitor Monteiro
# Data    : 28/05/2026
# '''

import random

def jogar(maximo, chances):
    numero_secreto = random.randint(1, maximo)
    acertou= False

    while chances > 0 an not acertou:
           palpite = int(input(Seu palpite (1 a " = str(maximo) = "): "))
                    
            if palpite == numero_secreto:
                print("🎉 Acertou!")
                acertou = True
            elif palpite < numero_secreto
                 print("📈 Muito baixo!")
            else:
                 print("📉 Muito alto")

            chances = chances - 1
             print"Chances restantes:", chances)

    return acertou

# === Níveis guardados em uma lista de listas: [nome, maximo, chances] ===
 niveis = [
       ["Fácil", 10, 3],
       ["Médio", 100, 5],
       ["Impossível", 1000, 10],
 ]

 # === Menu e escolha do nível ===
 print("Escolha o nível de dificuldade>")
 print("1 - Fácil     (1 a 10,  chances)")
 print("2 - Médio     (1 A 100, 5 chances)")
 print("3 - Impossível  (1 a 1000,10 chances)")
opcao = int(input("Digite 1, 2 ou 3: "))

# A opção 