/*
Problema: 1002 Beecrowd
Data: 22/09/2026
Autor: João Vitor Monteiro*/

#include <stdio.h>

int main() {
    double raio, area;
    double pi = 3.14159;

    
    if (scanf("%lf", &raio) == 1) {
        // Cálculo da área: A = π * R²
        area = pi * (raio * raio);

        
        printf("A=%.4lf\n", area);
    }

    return 0;
}