/*
Problema 1011 Beecrowd
Data: 22/09/2026
Autor: João Vitor Monteiro
*/

#include <stdio.h>

int main() {
    double R, volume;
    double pi = 3.14159;

    // Leitura do raio
    if (scanf("%lf", &R) == 1) {
        // Cálculo do volume com 4.0/3 para evitar divisão inteira
        volume = (4.0 / 3.0) * pi * (R * R * R);

        // Imprime a saída com 3 casas decimais e quebra de linha
        printf("VOLUME = %.3lf\n", volume);
    }

    return 0;
}