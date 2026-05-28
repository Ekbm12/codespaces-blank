'''
Problema: beecrowd | 1002
Data: 2026.04.07
Estudante: João Vitor Monteiro
'''
#Objetivo: calcular a área de uma circunferência e exibi-lá com 4 casas decimais

# --- ANÁLISE (LIAC) ---
#Entrada: um número de ponto flutuante (o raio R)
#Processamento: Eleva o valor do raio ao quadrado e mutiplica.
#Saída: exibir no formato "A= valor" com 4 casas decimais


R = float(input())

#
pi = 3.14159

A = pi * R ** 2


print(f"A= {A:.4f}")