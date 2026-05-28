'''
Problema: beecrowd | 1017
Data: 23.04.2026
Estudante: João Vitor Monteiro
'''
#Objetivo: Calcular quantos litros seriam necessários para em uma viagem.
#--- ANÁLISE (LIAC) ---
#Entrada: Número inteiro de horas e velocidade média digitado pelo teclado
#Processamento: Mutiplica o total de horas com a velocidade média e depois dividi a distância por doze
#Saída: exibir a quantidade de litros necessários para a viagem com três digitos após o ponto decimal

H = int(input())

# Velocidade Média
V = int(input())
# Multiplicar o total de horas com a velocidade média
D = H * V
# Dividir a distancia por doze
M = D / 12

print(f"{M:.3f}")