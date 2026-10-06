# ====================================
# Arquivo:  main.py
# Disciplina:   2026-PCAP
# Aula:         20
# Autor:  João Vitor Monteiro
# Data:     2026.08.04
# Conceitos:
# ======================================

# Importar funções de arquivos (módulos)
from telas import titulo, linha
from adivinhe import jogar_adivinhe
from ppt import jogar_ppt
from modulos import ler_opcao, ler_numero
from placar import carrega_placar,salva_placar

NOME_DO_DONO = 'JOÃO'
OPCOES = ('0', '1', '2', '3')

while True:
    titulo('FLIPERAMA DO ' + NOME_DO_DONO)
    print('1 - Jogo Adivinhe O Número')
    print('2 - Pedra-Papel-Tesoura')
    print('0 - Sair do fliperama')
    opcao = ler_opcao('Escolha uma opção:',OPCOES).strip()

    if opcao == '0':
        print('Até a Próxima!')
        break
    elif opcao == '1':
        jogar_adivinhe()
    elif opcao == '2':
        jogar_ppt()    

NOMES_DO_JOGOS = ['Adivinhe o Numero', 'Pedra-papel-Tesoura']

vezes_jogado = [0,0,0]


def mostra_placar():
    titulo('PLACAR')
    for i in range(3):
        print(NOMES_DO_JOGOS[i] + ':' + str(vezes_jogado) + 'x')

        if opcao == '0':
          mostra_placar()
          titulo('Ate a proxima!')
          break

        indice = int(opcao) - 1
        vezes_jogado[indice] = vezes_jogado[indice] + 1


from placar import salva_placar

if opcao == '0':
    mostra_placar
    salva_placar(vezes_jogado)
    titulo('Ate a proxima!')
    

from placar import salva_placar, carrega_placar
