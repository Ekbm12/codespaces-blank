'''
Problema: beecrowd | 1011
Data: 2026.04.07
Estudante: João Vitor Monteiro
'''
#Objetivo: Ler o raio de uma esfera e calcular seu volume com a fòrmula (4/3) + pi * R³

# --- ANÁLISE (LIAC) ---
#Entrada: um número de ponto flutuante (o raio R)
#Processamento: aplicar a fórmula do volume da esfera
#Saída: exibir no formato "VOLUME= valor" com 3 casas decimais

# float () -> converte o valor lido para número decimal (ponto flutuante)
R = float(input())

#
pi = 3.14159

# 4.0/3 garante divisão decimal (não inteira) - não usar math.pi
# R***3 -> R elevado á terceira potência (R³)
V = (4.0 / 3) * pi * R ** 3

# :.3f -> formata o número com exatamente 3 casas decimais
print(f"VOLUME = {V:.3f}")