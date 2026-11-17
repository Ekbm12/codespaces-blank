/*
* Disciplina    : 2026-PCAP
* Problema      : beecrowd 1011 - Esfera
* Autor         : João Vitor Monteiro
* LIAC          : calcular e mostrar o volume de uma esfera dado o seu raio $R$, utilizando a fórmula VOLUME e imprimindo o resultado com 3 casas decimais.
*/

#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double R, volume;
    double pi = 3.14159;

    // Leitura do raio
    if (cin >> R) {
        // Cálculo do volume usando 4.0/3.0 para evitar divisão inteira
        volume = (4.0 / 3.0) * pi * (R * R * R);

        // Formatação com 3 casas decimais fixas
        cout << fixed << setprecision(3);
        cout << "VOLUME = " << volume << endl;
    }

    return 0;
}
