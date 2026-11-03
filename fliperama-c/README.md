#Fliperama em C (MeuApp v3.0)

## O que e
[# Esse é um fliperama que inclui um jogo de adivinhar o número e jogadores cadastrados.]

## Como compilar e rodar
gcc -wall fliperama.c -o fliperama
./fliperama

## Arquivos
- fliperama.c: O fliperama em si
- jogadores.csv: O cadastro de jogadores.

## Python x C: o que mudou

| O que | No jogadores.py (Não havia o cadastro de jogadores usando .csv.) | No fliperama.c (Já no C,possui cadastro usando o .csv) |
|   |   |   |

| Guardar um jogador| jogadores.append(novo) (1. ) |strcpy(apelidos [qtd],novo) (1. ) |
| comparar apelidos | == (1.   ) | strcmp(...) == 0 (1. ) |
| Abrir sem arquivo | exists(ARQUIVO) (1.  ) |fopen == NULL (1. )|

## O que o C me obrigou a decidir
[O C me obrigou a decidir o número de apelidos e quantos eu deveria cadastrar. ]

## Autoavalliacao
Nesse projeto eu descobri como cadastrar jogadores usando o .csv|B|

|1. Estrutura,compilação e Git | A estrutura do fliperama permanece semelhante ao projeto em Python| a compilação é feita usando o comando "gcc -Wall (nome do projeto.c) -o (nome do projeto)
|2. Cadastro: menu, funcoes e vetores |O menu continua semelhante ao projeto em Python,usando os números para entrar na função preferida, as funcoes #ler_ servem para ler a função dada pelo usuário e mostrar uma mensagem na tela, o vetor #define servem para definir uma quantidade ou o nome de alguem.
|3. Jogo e partidas |O jogo é o adivinhe o número,onde o usuário terá que adivinhar o número enquanto o programa da dicas se ele está perto do número ou muito longe,no final do jogo,ele mostra quantas tentativas o jogador fez para adivinhar o número no final de cada partida.
|4. Persistencia | Eu tive bastantes erros durante a produção desse fliperama,porém mantive a calma e os corrigi.
|5. Documentação e comparação| No dia 28 de outubro,o fliperama ainda estava vazio e sem codigo,no mesmo dia,eu comecei a codifica-ló,no dia 29 eu continuei o processo e o terminei no mesmo dia,a comparação do mesmo projeto em Python para C é a dificuldade e como o codigo aumenta na outra linguagem.