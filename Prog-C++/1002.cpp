/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1002 - Área do Circulo
* Autor         : João Vitor Monteiro
* LIAC          : Realiza a leitura de um valor de ponto flutuante de dupla precisão (double) para o raio,e a impressão do resultado formatado com 4 casas decimais.
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double raio, area;
    double pi = 3.14159;

    // Leitura do raio
    if (cin >> raio) {
        // Cálculo da área
        area = pi * raio * raio;

        // Formata a saída para 4 casas decimais fixas
        cout << fixed << setprecision(4);
        cout << "A=" << area << endl;
    }

    return 0;
}