'''
Problema: beecrowd | 1008
Data: 2026.04.07
Estudantes: João Vitor Monteiro
'''
#--- ANÁLISE LIAC ---
# Entrada: Dois números inteiros e um decimal
# Processamento: Dividir o número de horas trabalhadas com o salário
# Saída: Exibir o número do funcionário e seu salário com 2 casas decimais
n = int(input())
h = int(input())
s = float(input())

st = h * s

print (f"NUMBER = {n}")
print (f"SALARY = U$ {st:.2f}")