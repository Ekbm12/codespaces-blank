/*
Programa: 1004.c
Data: 22/09/2026
Autor: João Vitor Monteiro
*/
#include <stdio.h>

int main() {
    int A, B, PROD;

    // Leitura dos dois valores inteiros
    if (scanf("%d %d", &A, &B) == 2) {
        // Cálculo do produto
        PROD = A * B;

        // Imprime a saída no formato exato: "PROD = X\n"
        printf("PROD = %d\n", PROD);
    }

    return 0;
}