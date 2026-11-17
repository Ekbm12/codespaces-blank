/*
* Disciplina: 2026-PCAP
* Problema  : beecrowd 1180 - Menor e Posicao
* Autor : João Vitor Monteiro
* LIAC  : Le N e depois N inteiros num vector. Imprime o menor valor e a posicao em que ele esta (apartir de zero),o vector sendo uma biblioteca como o cout.
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;

    if (cin >> N) {
        vector<int> X(N);

        // Leitura dos N elementos do vetor
        for (int i = 0; i < N; i++) {
            cin >> X[i];
        }

        // Inicializa o menor valor e a posição com o primeiro elemento (índice 0)
        int menor = X[0];
        int posicao = 0;

        // Percorre a partir do segundo elemento para encontrar o menor
        for (int i = 1; i < N; i++) {
            if (X[i] < menor) {
                menor = X[i];
                posicao = i;
            }
        }

        // Impressão no formato exato exigido
        cout << "Menor valor: " << menor << endl;
        cout << "Posicao: " << posicao << endl;
    }

    return 0;
}