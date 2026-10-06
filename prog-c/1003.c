/*
Problema: 1002 Beecrowd
Data: 22/09/2026
Autor: João Vitor Monteiro*/

#include <stdio.h>

int main() {
    int A, B, SOMA;

    // Leitura dos dois valores inteiros
    if (scanf("%d %d", &A, &B) == 2) {
        // Cálculo da soma
        SOMA = A + B;

        // Imprime a saída no formato exato exigido: "SOMA = X\n"
        printf("SOMA = %d\n", SOMA);
    }

    return 0;
}