/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1004 - Produto Basico
* Autor         : João Vitor Monteiro
* LIAC          : ler dois valores inteiros, calcular o produto (multiplicação) entre eles e atribuir o resultado à variável PROD, imprimindo no formato exato exigido.
*/

#include <iostream>

using namespace std;

int main() {
    int A, B, PROD;

    // Leitura dos dois valores inteiros
    if (cin >> A >> B) {
        // Cálculo do produto
        PROD = A * B;

        // Impressão no formato exato: "PROD = X" + quebra de linha
        cout << "PROD = " << PROD << endl;
    }

    return 0;
}