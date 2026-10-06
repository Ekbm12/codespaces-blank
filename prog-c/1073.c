/*
NOME: João Vitor Monteiro
Problema: 1073 Beecrowd
2026.09.29
*/

#include <stdio.h>

int main() {
    int N;

    if (scanf("%d", &N) == 1) {
        // Percorre de 2 até N, incrementando de 2 em 2 para pegar apenas os pares
        for (int i = 2; i <= N; i += 2) {
            printf("%d^2 = %d\n", i, i * i);
        }
    }

    return 0;
}