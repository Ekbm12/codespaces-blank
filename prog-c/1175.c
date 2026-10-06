/*
Disciplina  : 2026--PCAP
Autor   : João Vitor Monteiro
Problema    : 1175 Beecrowd
*/
#include <stdio.h>

int main(){
    int n[20], i;

    for(i = 0; i <20; i++) {
        scanf("%d", &n[i]);
    }

    for (i = 0; i <20; i++) {
        printf("N[%d] = %d\n", i, n[19-i]);

    }
return 0;
}