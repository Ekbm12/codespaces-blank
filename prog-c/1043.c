/*
NOME: João Vitor Monteiro
Problema: 1043 Beecrowd
2026.09.29
*/

#include <stdio.h>

int main() {
    double A, B, C;

    if (scanf("%lf %lf %lf", &A, &B, &C) == 3) {
        // Verifica a condição de existência do triângulo
        if ((A + B > C) && (A + C > B) && (B + C > A)) {
            double perimetro = A + B + C;
            printf("Perimetro = %.1lf\n", perimetro);
        } else {
            double area = ((A + B) * C) / 2.0;
            printf("Area = %.1lf\n", area);
        }
    }

    return 0;
}