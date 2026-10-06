/*
NOME: João Vitor Monteiro
Problema: 1044 Beecrowd
2026.09.29
*/


#include <stdio.h>

int main() {
    int A, B;

    // Leitura dos dois valores inteiros
    if (scanf("%d %d", &A, &B) == 2) {
        // Verifica se A é múltiplo de B OU se B é múltiplo de A
        if (A % B == 0 || B % A == 0) {
            printf("Sao Multiplos\n");
        } else {
            printf("Nao sao Multiplos\n");
        }
    }

    return 0;
}