'''
Problema: beecrowd | 1044
Data: 2026.04.16
Estudante: João Vitor Monteiro
'''
# Objetivo: Verificar se dois inteiros são mútiplos entre si

# --- ANÁLISE (LIAC) ---
# Entrada: dois inteiros A e B na mesma linha separados por espaço
# Processamento: indentificar maior e menor, verificar se maior % menor == 0
# Saída: "Sao Multiplos" ou "Nao sao Multiplos"

A, B = input().split()
A = int(A)
B = int(B)

# Identifica maior e menor para aplicar o operador % corretamente
# (o resto sempre deve ser calculado divindo o maior pelo menor)
if A > B:
    maior = A
    menor = B
else:
    maior = B
    menor = A

# Operador % (módulo): retorna o resto da divisão inteira
# Se o resto for 0, o maior é mútiplo do menor -> são mútiplos entre si
if maior % menor == 0:
    print ("Sao Multiplos")
else:
    print("Nao sao Multiplos")