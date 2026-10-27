/*
NOME: João Vitor Monteiro
Problema: 1044 Beecrowd
2026.09.29
*/


#include <stdio.h>

int main() {
    int N, X;

            if (scanf("%d", &N) == 1) {
                    for (int i = 0; i < N; i++) {
                                scanf("%d", &X);

                                            int eh_primo = 1; // Consideramos inicialmente que o número é primo (1 = verdadeiro)

                                                        // Testamos se algum número entre 2 e a raiz/metade de X consegue dividi-lo
                                                                    for (int j = 2; j * j <= X; j++) {
                                                                                    if (X % j == 0) {
                                                                                                        eh_primo = 0; // Se for divisível por outro número, não é primo
                                                                                                                            break;        // Interrompe a verificação para economizar tempo
                                                                                                                                            }
                                                                                                                                                        }

                                                                                                                                                                    // Impressão da resposta de acordo com a variável eh_primo
                                                                                                                                                                                if (eh_primo && X > 1) {
                                                                                                                                                                                                printf("%d eh primo\n", X);
                                                                                                                                                                                                            } else {
                                                                                                                                                                                                                            printf("%d nao eh primo\n", X);
                                                                                                                                                                                                                                        }
                                                                                                                                                                                                                                                }
                                                                                                                                                                                                                                                    }

                                                                                                                                                                                                                                                        return 0;
                                                                                                                                                                                                                                                        }
