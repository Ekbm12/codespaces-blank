/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1168 - LED
* Autor         : João Vitor Monteiro
* LIAC          : ler casos de teste e, para cada caso, ler um número inteiro muito grande. por isso deve ser lido como string) e calcular a quantidade total de LEDs necessários para exibi-lo em um painel de 7 segmentos.
*/

#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    // Vetor mapeando a quantidade de LEDs para os dígitos de 0 a 9
    int leds_por_digito[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    if (cin >> N) {
        while (N--) {
            string numero;
            cin >> numero;

            int total_leds = 0;

            // Percorre cada caractere da string e soma os LEDs correspondentes
            for (char c : numero) {
                total_leds += leds_por_digito[c - '0'];
            }

            cout << total_leds << " leds" << endl;
        }
    }

    return 0;
}
