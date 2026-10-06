/*
NOME: João Vitor Monteiro
Problema: 1078 Beecrowd
2026.09.29
*/

#include <stdio.h>

int main() {
    int N;

    if (scanf("%d", &N) == 1) {
        // Laço de 1 a 10 para calcular e exibir cada linha da tabuada
        for (int i = 1; i <= 10; i++) {
            printf("%d x %d = %d\n", i, N, i * N);
        }
    }

    return 0;
}