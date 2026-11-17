# fliperama em C++ (MeuApp v4.0)

## O que e
 o fliperama das aulas passadas,porem transferido
 para a linguagem C++.

# como compilar e rodar
g++ -Wall fliperama.cpp -o fliperama
./fliperama

## Arquivos
- fliperama.cpp: Como o nome já diz é um fliperama.
- jogadores.csv: Registro de jogadores, em uma coluna ele guarda o nome do jogador e o número de partidas jogadas.

## C x C++: o que mudou
| O que | No fliperama.c (linha) | No fliperama.cpp (linha)  |
| guardar um jogador | strcpy(apelidos [qtd], novo) (1.) | apelidos.push_back(novo) (1. ) |
| comparar apelidos | strcmp(...) = 0 (1. ) | == (1. ) |
| a funcao que cadastra | int cadastrar(..., int qtd) (1. ) | void cadastrar(... &apelidos, ...) (1. ) |

## O que C++ decidiu por mim
O numero de partidas jogadas pelo jogadores e o registro deles que agora é feito automaticamente


## Autoavaliacao
| Criterio | Conceito que espero | Onde se prova (arquivo e linha) |
| Senti meu desempenho melhorar conforme essa aula | A |o projeto em si.|
| 1. Estrutura, compilacao e Git |Numero de linhas | fiz todas as compilações pedidas | fiz todos os gits pedidos
| 2. Cadastro: vectors e referencia | cada vector server para registrar uma função do fliperama| #include <vector> para faze-los funcionarem|
| 3. Jogo e partidas O jogo é o advinhe o número assim como as aulas passadas| Joguei 7 partidas.|
| 4. Persistencia: Não tive muitos erros durante a escrita do codigo e me manti calmo durante o processo
| 5. Documentacao e comparacao: Terminei o fliperama no mesmo dia.